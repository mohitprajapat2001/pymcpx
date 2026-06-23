# LangChain

## BaseTool Pattern

All PyMCPX tools extend `langchain_core.tools.BaseTool`:

```python
from langchain_core.tools import BaseTool
from pymcpx.services.github.models import SearchRepositoriesInput

class GitHubSearchRepositoriesTool(BaseTool):
    name: str = "github_search_repositories"
    description: str = "Search GitHub repositories..."
    args_schema: type = SearchRepositoriesInput
    config: GitHubConfig | None = None

    def _run(self, **kwargs) -> dict:
        inp = SearchRepositoriesInput(**kwargs)
        client = _client_from_env(self.config)
        return client.search_repositories(inp).model_dump()

    async def _arun(self, **kwargs) -> dict:
        return self._run(**kwargs)
```

## Tool Registration with LangChain Agents

```python
from langchain.agents import create_tool_calling_agent
from pymcpx.services.github import (
    GitHubSearchRepositoriesTool,
    GitHubCreateIssueTool,
)

tools = [GitHubSearchRepositoriesTool(), GitHubCreateIssueTool()]
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
```

## Config Injection

Tools accept an optional explicit config (for testing / multi-tenant):

```python
config = GitHubConfig(token=SecretStr("ghp_..."))
tool = GitHubSearchRepositoriesTool(config=config)
```

Without config, tools read from environment variables automatically.

## Async

PyMCPX tools implement both `_run` (sync) and `_arun` (async).
For REST-only services, `_arun` delegates to `_run`.
For async-native clients, implement proper `async def _arun`.

## Tool Descriptions

Write descriptions as if they are instructions to an LLM:
- Say what the tool does and when to use it
- Mention key input fields
- Keep under 200 characters for prompt efficiency
