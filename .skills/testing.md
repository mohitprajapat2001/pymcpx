# Testing

## Test Categories

PyMCPX has three distinct test categories:

### 1. Service-Level Tests (`pymcpx/services/<name>/tests/`)

- Unit tests for models, utils, and simulation engine
- No network calls (use `GitHubSimulationEngine` or mock responses)
- Run per service: `pytest pymcpx/services/github/tests/`

### 2. Regression Tests (`pymcpx/regression_tests/<name>/`)

- Lock down the public API contract
- Detect tool name changes, model field removals, export surface changes
- Run across all releases to catch breaking changes
- Run: `pytest pymcpx/regression_tests/`

### 3. Scenario Tests (`pymcpx/scenario_tests/<name>/`)

- Multi-step, real-world agent workflows
- Use the simulation engine (no live API)
- Validate call sequences and output shapes
- Inspired by TauBench evaluation style
- Run: `pytest pymcpx/scenario_tests/`

## Running Tests

```bash
# All tests
pytest

# Via test runner script (recommended)
python scripts/test.py
python scripts/test.py --service github
python scripts/test.py --regression
python scripts/test.py --scenario
python scripts/test.py --unit
python scripts/test.py --cov

# Direct pytest
pytest pymcpx/services/github/tests/ -v
pytest pymcpx/regression_tests/github/ -v
pytest pymcpx/scenario_tests/github/ -v
```

## Simulation Engine Pattern

All tests use `GitHubSimulationEngine` (or the equivalent for each service).
This ensures:
- Tests are fast and deterministic
- No API keys required in CI
- Offline development works

```python
engine = GitHubSimulationEngine()
result = engine.run("github_search_repositories", {"query": "langchain"})
```

Register custom fixtures for specific test cases:
```python
engine.register(
    tool_name="github_create_issue",
    input_match={"title": "My Bug"},
    output={"id": 42, "number": 7, ...},
)
```

## Test File Naming

- Service tests: `test_<service>.py`
- Regression tests: `test_<service>_regression.py`
- Scenario tests: `test_<service>_scenarios.py`
