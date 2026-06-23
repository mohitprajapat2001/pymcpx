# Pydantic

## Version

PyMCPX uses **Pydantic v2** exclusively. No Pydantic v1 compatibility.

## Model Conventions

```python
from pydantic import BaseModel, Field, SecretStr

class MyConfig(BaseModel):
    api_key: SecretStr = Field(..., description="Secret API key.")
    timeout: int = Field(default=30, ge=1, le=300)
    model_config = {"frozen": True}   # configs are immutable
```

## Secrets

Use `SecretStr` for all tokens and API keys. Access with `.get_secret_value()`.

```python
token = config.token.get_secret_value()
```

## Validators

Use `@field_validator` (not deprecated `@validator`):

```python
@field_validator("query")
@classmethod
def query_not_blank(cls, v: str) -> str:
    if not v.strip():
        raise ValueError("query must not be blank")
    return v.strip()
```

## Model Serialization

```python
model.model_dump()           # to dict
model.model_dump_json()      # to JSON string
Model.model_validate(data)   # from dict (replaces .parse_obj)
Model.model_json_schema()    # JSON Schema (used for MCP)
```

## Annotated Fields

Prefer `Annotated` for reusable constraint types:

```python
from typing import Annotated
PositiveInt = Annotated[int, Field(ge=1)]
```

## Input vs Output Models

- Input models: named `<Operation>Input` (e.g. `SearchRepositoriesInput`)
- Output models: named `<Resource>Model` or `<Operation>Output`
- Config model: named `<Service>Config` (always frozen)
