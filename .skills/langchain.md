# LangChain

## BaseTool Pattern

All PyMCPX tools extend `langchain_core.tools.BaseTool`:

```python
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

class BinaryFloatInput(BaseModel):
    a: float = Field(description="First operand")
    b: float = Field(description="Second operand")

class AddTool(BaseTool):
    name: str = "add_numbers"
    description: str = "Add two numbers together and return their sum."
    args_schema: type[BaseModel] = BinaryFloatInput

    def _run(self, a: float, b: float, **kwargs) -> str:
        return str(a + b)

    async def _arun(self, **kwargs) -> str:
        return self._run(**kwargs)
```

## Tool Registration with LangChain Agents

```python
from langchain.agents import create_tool_calling_agent
from pymcpx.services.calculator import AddTool, DivideTool

tools = [AddTool(), DivideTool()]
agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
```

## Config Injection

Tools can accept an optional explicit config (for testing / multi-tenant):

## Async

PyMCPX tools implement both `_run` (sync) and `_arun` (async).
For REST-only services, `_arun` delegates to `_run`.
For async-native clients, implement proper `async def _arun`.

## Tool Descriptions

Write descriptions as if they are instructions to an LLM:
- Say what the tool does and when to use it
- Mention key input fields
- Keep under 200 characters for prompt efficiency
