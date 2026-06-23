# Coding Style

## Formatter & Linter

PyMCPX uses **Ruff** exclusively — no Black, no separate isort.

```bash
ruff check .          # lint
ruff check --fix .    # lint + auto-fix
ruff format .         # format
```

## Key Rules

- Line length: **100 characters**
- Target: **Python 3.11+**
- Quotes: **double quotes**
- Import order: managed by Ruff's isort (`I` rule set)
- `from __future__ import annotations` on every file that uses type hints

## Naming Conventions

| Entity | Convention | Example |
|--------|-----------|---------|
| Classes | PascalCase | `GitHubSearchRepositoriesTool` |
| Functions/methods | snake_case | `build_headers()` |
| Constants | UPPER_SNAKE | `MCP_TOOLS` |
| Modules | snake_case | `tools.py`, `simulation/` |
| Private symbols | leading underscore | `_GitHubClient` |

## Type Annotations

- Use `from __future__ import annotations` for deferred evaluation
- Prefer `X | None` over `Optional[X]`
- Prefer `list[str]` over `List[str]`
- Use `Annotated[T, Field(...)]` for Pydantic field metadata

## Docstrings

- Google-style docstrings on all public classes, methods, and functions
- Module-level docstrings describe purpose and show usage examples
- Private helpers (`_`) can have shorter docstrings

## No Placeholders

Every file should be complete. Stubs use `# TODO:` comments but are
never left with `pass` bodies in public-facing code.
