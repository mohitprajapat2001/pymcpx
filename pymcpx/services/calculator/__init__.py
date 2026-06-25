"""
pymcpx.services.calculator
--------------------------
MCP-compatible LangChain tools for basic arithmetic operations.

Quick start
-----------
Import individual tools::

    from pymcpx.services.calculator import AddTool, DivideTool

Use the toolkit to get all tools at once::

    from pymcpx.services.calculator import CalculatorToolkit

    tools = CalculatorToolkit().get_tools()

Or register all tools with your MCP server::

    from pymcpx.services.calculator import MCP_TOOLS
    mcp_server.register_tools(MCP_TOOLS)
"""

from pymcpx.services.calculator.arithmetic_tools import (
    MCP_TOOLS,
    AbsTool,
    AddTool,
    BinaryFloatInput,
    BinaryIntInput,
    CalculatorToolkit,
    DivideTool,
    ModuloTool,
    MultiplyTool,
    PowerTool,
    SqrtTool,
    SubtractTool,
    UnaryFloatInput,
)

__all__ = [
    # MCP tools list
    "MCP_TOOLS",
    "AbsTool",
    # Tools
    "AddTool",
    # Input schemas
    "BinaryFloatInput",
    "BinaryIntInput",
    # Toolkit
    "CalculatorToolkit",
    "DivideTool",
    "ModuloTool",
    "MultiplyTool",
    "PowerTool",
    "SqrtTool",
    "SubtractTool",
    "UnaryFloatInput",
]
