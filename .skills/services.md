# Services

## Service Responsibilities

Each service sub-package in `pymcpx/services/<name>/` follows this exact layout:

```
<name>/
├── __init__.py      ← re-exports full public API
├── models.py        ← Pydantic config + input + output models
├── tools.py         ← LangChain BaseTool subclasses + MCP_TOOLS
├── utils.py         ← helpers (headers, errors, pagination, strings)
├── .env.example     ← required environment variables
├── README.md        ← service-specific documentation
├── simulation/      ← offline engine for testing + evaluation
│   ├── __init__.py
│   ├── engine.py    ← SimulationEngine class
│   ├── models.py    ← SimulatedResponse, SimulationCall
│   └── utils.py     ← inputs_match(), deep_merge()
└── tests/
    ├── __init__.py
    └── test_<name>.py
```

## Creating a New Service

```bash
python scripts/create_service.py <service_name>
```

Then implement:
1. `models.py` — config model, input/output models per operation
2. `utils.py` — headers, error class, any parsing helpers
3. `tools.py` — BaseTool subclasses + MCP_TOOLS
4. `simulation/engine.py` — SimulationEngine with built-in fixtures
5. `tests/test_<name>.py` — unit tests using simulation
6. Update `__init__.py` to re-export everything

Reference: `pymcpx/services/github/` is the canonical implementation.

## Installation Strategy

```bash
pip install pymcpx           # core only (pydantic + dotenv)
pip install pymcpx[github]   # GitHub + langchain-core + requests
pip install pymcpx[slack]    # Slack + langchain-core + slack-sdk
pip install pymcpx[all]      # all services
```

Service extras are declared in `pyproject.toml [project.optional-dependencies]`.
Add a new section for each service you add.

## Service Configuration

All services accept a typed `Config` model:

```python
config = GitHubConfig(token=SecretStr(os.environ["GITHUB_TOKEN"]))
tool = GitHubSearchRepositoriesTool(config=config)
```

Or fall back to environment variables automatically:
```python
tool = GitHubSearchRepositoriesTool()  # reads GITHUB_TOKEN from env
```
