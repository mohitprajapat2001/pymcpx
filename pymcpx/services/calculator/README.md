# Calculator Service

MCP-compatible LangChain tools for basic arithmetic operations.

## Installation

Install the calculator extra:

```bash
pip install pymcpx[calculator]
```

## Tools

| Tool Name | Class | Description | Input Schema |
|-----------|-------|-------------|--------------|
| `add_numbers` | `AddTool` | Add two numbers | `a: float, b: float` |
| `subtract_numbers` | `SubtractTool` | Subtract second number from first | `a: float, b: float` |
| `multiply_numbers` | `MultiplyTool` | Multiply two numbers | `a: float, b: float` |
| `divide_numbers` | `DivideTool` | Divide first number by second | `a: float, b: float` |
| `power_numbers` | `PowerTool` | Raise first number to power of second | `a: float, b: float` |
| `modulo_numbers` | `ModuloTool` | Return remainder of division | `a: float, b: float` |
| `sqrt_number` | `SqrtTool` | Return square root of non-negative number | `a: float` |
| `abs_number` | `AbsTool` | Return absolute value of number | `a: float` |

## Usage

### Individual Tools

```python
from pymcpx.services.calculator import AddTool

tool = AddTool()
result = tool.invoke({"a": 3, "b": 4})
print(result)  # "7"
```

### Toolkit

You can retrieve all calculator tools at once using the `CalculatorToolkit`:

```python
from pymcpx.services.calculator import CalculatorToolkit

toolkit = CalculatorToolkit()
tools = toolkit.get_tools()
```

### MCP Integration

Register all tools with your MCP server:

```python
from pymcpx.services.calculator import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```
