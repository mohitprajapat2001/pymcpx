# Converter Service

MCP-compatible LangChain tools for unit conversions.

## Installation

Install the converter extra:

```bash
pip install pymcpx[converter]
```

## Tools

| Tool Name | Class | Description | Input Schema |
|-----------|-------|-------------|--------------|
| `convert_length` | `ConvertLengthTool` | Convert length values (e.g. m, cm, mm, km, inch, ft, yard, mile) | `value: float, from_unit: str, to_unit: str` |
| `convert_weight` | `ConvertWeightTool` | Convert weight values (e.g. kg, g, mg, lb, oz) | `value: float, from_unit: str, to_unit: str` |
| `convert_temperature` | `ConvertTemperatureTool` | Convert temperature values (e.g. Celsius, Fahrenheit, Kelvin) | `value: float, from_unit: str, to_unit: str` |

## Usage

### Individual Tools

```python
    from pymcpx.converter import ConvertLengthTool

tool = ConvertLengthTool()
result = tool.invoke({"value": 1.5, "from_unit": "m", "to_unit": "cm"})
print(result)  # "150"
```

### Toolkit

```python
    from pymcpx.converter import ConverterToolkit

toolkit = ConverterToolkit()
tools = toolkit.get_tools()
```

### MCP Integration

Register all tools with your MCP server:

```python
    from pymcpx.converter import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```
