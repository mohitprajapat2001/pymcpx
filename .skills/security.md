# Security

## Secrets Management

- **Never** hardcode tokens, API keys, or passwords in source code
- Use `SecretStr` from Pydantic for all sensitive fields
- Load from environment variables via `python-dotenv`
- Create a `.env` file for local secrets — never commit `.env` to the repository

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

## Dependency Security

- Pin dependency versions in `pyproject.toml`
- Run `pip audit` in CI (optional but recommended)
