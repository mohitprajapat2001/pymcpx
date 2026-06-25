# Testing

## Running Tests

```bash
# All tests
pytest

# Per service
pytest pymcpx/services/
```

## Continuous Integration

The ``.github/workflows/tests.yml`` workflow runs on **every push and every pull request**.
It executes all tests against Python 3.11 and 3.12 with coverage, and uploads results to Codecov.
No API keys are required — all tests use the simulation engine.

## Simulation Engine Pattern

Tests use `DatetimeSimulationEngine` (or the equivalent for each service).
This ensures:
- Tests are fast and deterministic
- No API keys required in CI
- Offline development works

```python
engine = DatetimeSimulationEngine()
result = engine.run("get_current_time", {"timezone": "UTC"})
```

Register custom fixtures for specific test cases:
```python
engine.register(
    tool_name="get_current_time",
    input_match={"timezone": "UTC"},
    output="2026-01-01T00:00:00Z",
)
```

## Test File Naming

- Service tests: `test_<service>.py`
