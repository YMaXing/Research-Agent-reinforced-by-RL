# Research Agent with Intermediate Rewards
### Extending Search-R1 via Prompt Engineering, AWS & Aviary RL Training

## Cost Estimate
| Sample Size | Estimated Cost |
|---|---|
| 10 questions | ~$0.80 |
| 20 questions | ~$1.60 |
| 50 questions | ~$4.00 |
| 200 questions | ~$16.00 ⚠️ |

---

## Dataset
We use [HotpotQA](https://hotpotqa.github.io/) (Yang et al., 2018) — a multi-hop question answering benchmark requiring reasoning across two Wikipedia articles. It is loaded automatically via HuggingFace `datasets` and cached locally on first run.

---

## Dependencies
See `requirements.txt`. Key libraries:
- `openai` — GPT-4o policy LLM + text-embedding-3-small
- `tavily-python` — external search engine (environment)
- `datasets` — HotpotQA loading via HuggingFace
- `python-dotenv` — secure API key management

---

## References
- Jin et al. (2025). *Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning.* arXiv:2503.09516
- Narayanan et al. (2024). *Aviary: Training Language Agents on Challenging Scientific Tasks.* arXiv:2412.21154
- Yang et al. (2018). *HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering.*