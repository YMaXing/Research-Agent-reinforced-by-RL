import os
import socket
import subprocess
import sys
import time
from pathlib import Path


def load_env_file(env_file: Path) -> None:
    """Load simple KEY=VALUE pairs from a dotenv file into process env."""
    if not env_file.exists():
        return

    for raw_line in env_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        # Keep values already exported in shell and only fill missing ones.
        os.environ.setdefault(key, value)


def resolve_python_executable(project_dir: Path) -> Path:
    """Resolve Python executable, preferring project-local virtual environments."""
    candidates = [
        project_dir / ".venv" / "Scripts" / "python.exe",
        project_dir / ".venv" / "bin" / "python",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return Path(sys.executable)


def make_env_with_pythonpath(project_dir: Path) -> dict[str, str]:
    """Build env vars with project paths added to PYTHONPATH."""
    env = os.environ.copy()
    pythonpath_parts = []

    current_pythonpath = env.get("PYTHONPATH")
    if current_pythonpath:
        pythonpath_parts.append(current_pythonpath)

    pythonpath_parts.append(str(project_dir))
    src_dir = project_dir / "src"
    if src_dir.exists():
        pythonpath_parts.append(str(src_dir))

    env["PYTHONPATH"] = os.pathsep.join(pythonpath_parts)
    return env


def wait_for_port(host: str, port: int, process: subprocess.Popen, service_name: str, timeout: int = 120) -> None:
    """Wait for TCP port to become reachable or fail early if process exits."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        if process.poll() is not None:
            raise RuntimeError(f"{service_name} exited early with code {process.returncode}")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((host, port)) == 0:
                return
        time.sleep(1)

    raise TimeoutError(f"Timed out waiting for {service_name} on {host}:{port}")


def terminate_process(process: subprocess.Popen, service_name: str) -> None:
    """Gracefully terminate a subprocess."""
    if process.poll() is not None:
        return

    print(f"Stopping {service_name}...")
    process.terminate()
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def assert_process_running(process: subprocess.Popen, service_name: str) -> None:
    """Raise if the process has exited."""
    if process.poll() is not None:
        raise RuntimeError(f"{service_name} exited with code {process.returncode}")


if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    home_dir = script_dir.parent

    nova_server_dir = home_dir / "research_agent_part_local" / "mcp_server"
    brown_server_dir = home_dir / "writing_workflow"
    composed_server_dir = script_dir / "mcp_server"
    mcp_client_dir = script_dir / "mcp_client"
    composed_server_config = script_dir / "mcp_servers_config_http.json"
    composed_client_config = script_dir / "mcp_composed_server_config_http.json"
    
    # Load optional shared env plus project-specific env files.
    load_env_file(script_dir / ".env")
    load_env_file(script_dir / "mcp_client" / ".env")
    load_env_file(nova_server_dir / ".env")
    load_env_file(brown_server_dir / ".env")

    # Ensure Opik project has a default name when key/workspace are provided.
    os.environ.setdefault("OPIK_PROJECT_NAME", "nova-brown-composed")

    nova_python = resolve_python_executable(nova_server_dir)
    brown_python = resolve_python_executable(brown_server_dir)
    # Reuse Nova interpreter for composed server because both require FastMCP.
    composed_python = nova_python
    client_python = nova_python

    print("Starting MCP servers as HTTP services...")

    nova_proc = subprocess.Popen(
        [str(nova_python), "-m", "src.server", "--transport", "streamable-http", "--port", "8001"],
        cwd=nova_server_dir,
        env=make_env_with_pythonpath(nova_server_dir),
    )
    brown_proc = subprocess.Popen(
        [str(brown_python), "-m", "brown.mcp.server", "--transport", "streamable-http", "--port", "8002"],
        cwd=brown_server_dir,
        env=make_env_with_pythonpath(brown_server_dir),
    )

    composed_proc: subprocess.Popen | None = None

    try:
        print("Waiting for Nova server on port 8001...")
        wait_for_port("127.0.0.1", 8001, nova_proc, "Nova MCP server", timeout=120)
        assert_process_running(nova_proc, "Nova MCP server")

        print("Waiting for Brown server on port 8002...")
        wait_for_port("127.0.0.1", 8002, brown_proc, "Brown MCP server", timeout=120)
        assert_process_running(brown_proc, "Brown MCP server")

        print("Nova and Brown servers are running")

        # Start composed server after upstream servers are confirmed reachable.
        composed_proc = subprocess.Popen(
            [
                str(composed_python),
                "-m",
                "src.main",
                "--transport",
                "streamable-http",
                "--port",
                "8003",
                "--config",
                str(composed_server_config),
            ],
            cwd=composed_server_dir,
            env=make_env_with_pythonpath(composed_server_dir),
        )

        print("Waiting for composed server on port 8003...")
        wait_for_port("127.0.0.1", 8003, composed_proc, "Composed MCP server", timeout=120)
        assert_process_running(composed_proc, "Composed MCP server")
        print("Composed server is running on port 8003")

        client_env = make_env_with_pythonpath(mcp_client_dir)
        subprocess.run(
            [str(client_python), "-m", "src.client", "--config", str(composed_client_config)],
            cwd=mcp_client_dir,
            env=client_env,
            check=True,
        )
    except Exception as exc:
        print(f"Launcher failed: {exc}")
        raise
    finally:
        terminate_process(nova_proc, "Nova MCP server")
        terminate_process(brown_proc, "Brown MCP server")
        if composed_proc is not None:
            terminate_process(composed_proc, "Composed MCP server")