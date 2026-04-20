import base64

import httpx

INVALID_IMAGE_DOMAINS = ["github"]

# OpenAI vision API only accepts these MIME types for inline images.
_OPENAI_ACCEPTED_IMAGE_TYPES = {"image/jpeg", "image/png", "image/webp", "image/gif"}


async def is_image_url_valid(url: str, timeout: float = 5.0) -> bool:
    return is_image_domain_accepted(url) and await ping(url, timeout)


def is_image_domain_accepted(url: str) -> bool:
    return not any(domain in url for domain in INVALID_IMAGE_DOMAINS)


async def ping(url: str, timeout: float = 5.0) -> bool:
    """
    Check if a URL is valid and reachable (returns HTTP 200) without redirects.

    Args:
        url: The URL to check.
        timeout: Timeout in seconds for the request.

    Returns:
        True if the URL is reachable and returns HTTP 200 with no redirect,
        False otherwise.

    Example:
        >>> import asyncio
        >>> asyncio.run(is_url_valid("https://www.google.com"))
        True
    """

    try:
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=False) as client:
            # Prefer HEAD to avoid downloading bodies when possible
            response = await client.head(url)

            # Some servers don't implement HEAD correctly or omit headers
            # Fallback to GET with an image-only Accept header
            if response.status_code == 405 or not response.headers.get("Content-Type"):
                response = await client.get(
                    url,
                    headers={
                        "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
                        "User-Agent": "brown-bot/1.0",
                    },
                )

            # Must be a successful response
            if response.status_code != 200:
                return False

            # Validate content type — only accept image types supported by OpenAI vision API
            content_type = response.headers.get("Content-Type", "").split(";")[0].strip().lower()
            if content_type not in _OPENAI_ACCEPTED_IMAGE_TYPES:
                return False

            return True
    except (httpx.RequestError, httpx.HTTPStatusError, httpx.TimeoutException, httpx.InvalidURL):
        return False


async def fetch_image_as_data_uri(url: str, timeout: float = 10.0) -> str | None:
    """Download an image and return it as a base64 data URI, or None on failure.

    Use this when the target API fetches image URLs server-side (and may be blocked
    by 403/auth) — encoding the image locally avoids the remote-fetch entirely.
    """
    try:
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
            response = await client.get(
                url,
                headers={
                    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
                    "User-Agent": "Mozilla/5.0 (compatible; brown-bot/1.0)",
                },
            )
            if response.status_code != 200:
                return None
            content_type = response.headers.get("Content-Type", "").split(";")[0].strip().lower()
            if content_type not in _OPENAI_ACCEPTED_IMAGE_TYPES:
                return None
            b64 = base64.b64encode(response.content).decode("ascii")
            return f"data:{content_type};base64,{b64}"
    except (httpx.RequestError, httpx.HTTPStatusError, httpx.TimeoutException, httpx.InvalidURL):
        return None
