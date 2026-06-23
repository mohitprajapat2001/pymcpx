# Security

## Secrets Management

- **Never** hardcode tokens, API keys, or passwords in source code
- Use `SecretStr` from Pydantic for all sensitive fields
- Load from environment variables via `python-dotenv`
- Each service has a `.env.example` — copy to `.env`, fill in, never commit `.env`

```python
from pydantic import SecretStr
from dotenv import load_dotenv

load_dotenv()
token = SecretStr(os.environ["GITHUB_TOKEN"])
```

## `.gitignore` Rules

The root `.gitignore` already excludes:
- `.env` (but NOT `.env.example`)
- `token.json` (OAuth2 token cache)
- `credentials.json` (Google OAuth2 credentials)

## Logging

- **Never** log secret values, tokens, or API keys
- Use `config.token.get_secret_value()` only in actual HTTP headers, not logs
- Pydantic `SecretStr` displays as `'**********'` in repr/logs automatically

## Input Validation

All tool inputs go through Pydantic models before reaching the API.
This prevents injection attacks and malformed requests.

```python
inp = SearchRepositoriesInput(**kwargs)  # validated ✅
```

## Token Scopes

Document the minimum required token scopes in each service's README:
- GitHub: specify which scopes are needed per tool
- Slack: specify which bot token scopes are needed
- etc.

## Dependency Security

- Pin dependency versions in `pyproject.toml`
- Run `pip audit` in CI (optional but recommended)
- Use trusted publishing for PyPI (no `PYPI_TOKEN` secret in Actions)
