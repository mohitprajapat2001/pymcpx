# PyMCPX

> **MCP-compatible LangChain tools for GitHub, Slack, Jira, Gmail, Notion, and more.**

[![CI](https://github.com/your-org/pymcpx/actions/workflows/ci.yml/badge.svg)](https://github.com/your-org/pymcpx/actions/workflows/ci.yml)
[![Tests](https://github.com/your-org/pymcpx/actions/workflows/tests.yml/badge.svg)](https://github.com/your-org/pymcpx/actions/workflows/tests.yml)
[![PyPI](https://img.shields.io/pypi/v/pymcpx.svg)](https://pypi.org/project/pymcpx/)
[![Python](https://img.shields.io/pypi/pyversions/pymcpx.svg)](https://pypi.org/project/pymcpx/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Features

- 🔌 **MCP-compatible** — every tool exposes a stable name and JSON schema consumable by any MCP host
- 🦜 **LangChain-native** — each tool extends `BaseTool` with typed `args_schema`
- 🧱 **Pydantic v2** — validated inputs, frozen configs, `SecretStr` for credentials
- 🧪 **Simulation engine** — run agent workflows offline without any API keys
- 📦 **Service extras** — install only what you need: `pip install pymcpx[github]`
- 🧬 **Regression + scenario tests** — lock API contracts and validate multi-step workflows

---

## Installation

```bash
# Core package (no service dependencies)
pip install pymcpx

# Specific service
pip install pymcpx[github]
pip install pymcpx[slack]
pip install pymcpx[jira]
pip install pymcpx[gmail]
pip install pymcpx[notion]

# All services
pip install pymcpx[all]

# Development
pip install pymcpx[dev]
# or
python scripts/bootstrap.py
```

---

## Quick Start

### GitHub

```python
import os
from dotenv import load_dotenv
from pydantic import SecretStr

from pymcpx.services.github import (
    GitHubConfig,
    GitHubSearchRepositoriesTool,
    GitHubCreateIssueTool,
)

load_dotenv()
config = GitHubConfig(token=SecretStr(os.environ["GITHUB_TOKEN"]))

# Search repositories
search = GitHubSearchRepositoriesTool(config=config)
result = search.run({"query": "langchain language:python stars:>500"})
print(result["items"][0]["full_name"])

# Create an issue
create_issue = GitHubCreateIssueTool(config=config)
issue = create_issue.run({
    "owner": "my-org",
    "repo": "my-repo",
    "title": "Bug: crash on startup",
    "body": "Steps to reproduce...",
})
print(issue["html_url"])
```

### Offline Simulation (No API Key Needed)

```python
from pymcpx.services.github import GitHubSimulationEngine

engine = GitHubSimulationEngine()

result = engine.run("github_search_repositories", {"query": "fastapi"})
print(result["items"][0]["full_name"])  # → acme-org/example-repo

# Inspect the call history
for call in engine.history:
    print(f"{call.tool_name}: {call.inputs}")
```

### MCP Registration

```python
from pymcpx.services.github.tools import MCP_TOOLS

# Register all 7 GitHub tools with your MCP server
mcp_server.register_tools(MCP_TOOLS)
```

---

## Services

For full details on the tools, schemas, and offline simulation engines of each service, refer to their respective service-level `README.md` files:

| Service        | Status         | Install Extra        | Documentation                                  |
| -------------- | -------------- | -------------------- | ---------------------------------------------- | --- |
| **Calculator** | ✅ Ready       | `pymcpx[calculator]` | [README](pymcpx/services/calculator/README.md) |
| **Datetime**   | ✅ Ready       | `pymcpx[datetime]`   | [README](pymcpx/services/datetime/README.md)   |
| **Converter**  | ✅ Ready       | `pymcpx[converter]`  | [README](pymcpx/services/converter/README.md)  |
| **GitHub**     | 🚧 Coming Soon | `pymcpx[github]`     | —                                              |
| **Slack**      | 🚧 Coming Soon | `pymcpx[slack]`      | —                                              |
| **Jira**       | 🚧 Coming Soon | `pymcpx[jira]`       | —                                              |
| **Gmail**      | 🚧 Coming Soon | `pymcpx[gmail]`      | —                                              |
| **Notion**     | 🚧 Coming Soon | `pymcpx[notion]`     | —                                              |     |

**Planned:** GitLab, Linear, Discord, Google Drive, Weather, News, SerpAPI, Reddit, LinkedIn, YouTube, Twitter

---

## Project Structure

```
pymcpx/
├── pymcpx/
│   ├── services/
│   │   ├── github/           ← reference implementation
│   │   │   ├── __init__.py   ← public API re-exports
│   │   │   ├── tools.py      ← LangChain tools + MCP_TOOLS
│   │   │   ├── models.py     ← Pydantic models
│   │   │   ├── utils.py      ← helpers
│   │   │   ├── simulation/   ← offline engine
│   │   │   └── tests/        ← unit tests
│   │   ├── slack/            ← stub
│   │   ├── jira/             ← stub
│   │   ├── gmail/            ← stub
│   │   └── notion/           ← stub
│   ├── regression_tests/     ← API contract tests
│   ├── scenario_tests/       ← multi-step workflow tests
│   └── skills/               ← shared primitives
├── .skills/                  ← project knowledge base
├── scripts/
│   ├── bootstrap.py          ← dev environment setup
│   ├── create_service.py     ← scaffold a new service
│   ├── test.py               ← test runner
│   └── release.py            ← version bumper
├── .github/workflows/        ← CI, tests, publish
└── pyproject.toml

```

## Adding a New Service

```bash
python scripts/create_service.py linear
```

This scaffolds all required files. Then implement `models.py`, `tools.py`,
`simulation/engine.py`, and tests following the GitHub service as reference.

---

## Contributing

## See [`.skills/contributing.md`](.skills/contributing.md) for the full guide.

## License

MIT © PyMCPX Contributors
