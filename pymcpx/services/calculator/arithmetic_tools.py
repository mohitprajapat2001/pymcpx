"""
Calculator arithmetic tools — MCP-compatible LangChain tools for basic math operations.

Available tools
---------------
- AddTool          : add two numbers
- SubtractTool     : subtract b from a
- MultiplyTool     : multiply two numbers
- DivideTool       : divide a by b (guards against division by zero)
- PowerTool        : raise a to the power of b
- ModuloTool       : remainder of a divided by b
- SqrtTool         : square root of a non-negative number
- AbsTool          : absolute value of a number
- CalculatorToolkit: convenience bundle that returns all tools at once
"""

from __future__ import annotations

import math
from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

# ---------------------------------------------------------------------------
# Shared input schemas
# ---------------------------------------------------------------------------


class BinaryIntInput(BaseModel):
    """Two integer operands."""

    a: int = Field(description="First operand (integer)")
    b: int = Field(description="Second operand (integer)")


class BinaryFloatInput(BaseModel):
    """Two float operands."""

    a: float = Field(description="First operand")
    b: float = Field(description="Second operand")


class UnaryFloatInput(BaseModel):
    """Single float operand."""

    a: float = Field(description="The operand")


# ---------------------------------------------------------------------------
# Addition
# ---------------------------------------------------------------------------


class AddTool(BaseTool):
    """Add two numbers together."""

    name: str = "add_numbers"
    description: str = "Add two numbers together and return their sum. Accepts integers or floats."
    args_schema: type[BaseModel] = BinaryFloatInput

    def _run(self, a: float, b: float, **kwargs: Any) -> str:
        result = a + b
        return _fmt(result)


# ---------------------------------------------------------------------------
# Subtraction
# ---------------------------------------------------------------------------


class SubtractTool(BaseTool):
    """Subtract b from a."""

    name: str = "subtract_numbers"
    description: str = "Subtract the second number from the first and return the difference."
    args_schema: type[BaseModel] = BinaryFloatInput

    def _run(self, a: float, b: float, **kwargs: Any) -> str:
        result = a - b
        return _fmt(result)


# ---------------------------------------------------------------------------
# Multiplication
# ---------------------------------------------------------------------------


class MultiplyTool(BaseTool):
    """Multiply two numbers together."""

    name: str = "multiply_numbers"
    description: str = "Multiply two numbers together and return the product."
    args_schema: type[BaseModel] = BinaryFloatInput

    def _run(self, a: float, b: float, **kwargs: Any) -> str:
        result = a * b
        return _fmt(result)


# ---------------------------------------------------------------------------
# Division
# ---------------------------------------------------------------------------


class DivideTool(BaseTool):
    """Divide a by b with zero-division guard."""

    name: str = "divide_numbers"
    description: str = (
        "Divide the first number by the second and return the quotient. "
        "Returns an error message when the divisor is zero."
    )
    args_schema: type[BaseModel] = BinaryFloatInput

    def _run(self, a: float, b: float, **kwargs: Any) -> str:
        if b == 0:
            return "Error: Division by zero is undefined."
        result = a / b
        return _fmt(result)


# ---------------------------------------------------------------------------
# Exponentiation
# ---------------------------------------------------------------------------


class PowerTool(BaseTool):
    """Raise a to the power of b."""

    name: str = "power_numbers"
    description: str = "Raise the first number to the power of the second number (a ** b)."
    args_schema: type[BaseModel] = BinaryFloatInput

    def _run(self, a: float, b: float, **kwargs: Any) -> str:
        try:
            result = a**b
        except (ValueError, ZeroDivisionError) as exc:
            return f"Error: {exc}"
        return _fmt(result)


# ---------------------------------------------------------------------------
# Modulo
# ---------------------------------------------------------------------------


class ModuloTool(BaseTool):
    """Remainder of a divided by b."""

    name: str = "modulo_numbers"
    description: str = (
        "Return the remainder when the first number is divided by the second (a % b). "
        "Returns an error message when the divisor is zero."
    )
    args_schema: type[BaseModel] = BinaryFloatInput

    def _run(self, a: float, b: float, **kwargs: Any) -> str:
        if b == 0:
            return "Error: Modulo by zero is undefined."
        result = a % b
        return _fmt(result)


# ---------------------------------------------------------------------------
# Square Root
# ---------------------------------------------------------------------------


class SqrtTool(BaseTool):
    """Square root of a non-negative number."""

    name: str = "sqrt_number"
    description: str = (
        "Return the square root of a non-negative number. "
        "Returns an error message for negative inputs."
    )
    args_schema: type[BaseModel] = UnaryFloatInput

    def _run(self, a: float, **kwargs: Any) -> str:
        if a < 0:
            return "Error: Square root of a negative number is not real."
        result = math.sqrt(a)
        return _fmt(result)


# ---------------------------------------------------------------------------
# Absolute Value
# ---------------------------------------------------------------------------


class AbsTool(BaseTool):
    """Absolute value of a number."""

    name: str = "abs_number"
    description: str = "Return the absolute (non-negative) value of a number."
    args_schema: type[BaseModel] = UnaryFloatInput

    def _run(self, a: float, **kwargs: Any) -> str:
        return _fmt(abs(a))


# ---------------------------------------------------------------------------
# Toolkit helper
# ---------------------------------------------------------------------------


class CalculatorToolkit:
    """Convenience bundle that exposes all calculator tools."""

    @classmethod
    def get_tools(cls) -> list[BaseTool]:
        """Return a list of every calculator tool instance."""
        return [
            AddTool(),
            SubtractTool(),
            MultiplyTool(),
            DivideTool(),
            PowerTool(),
            ModuloTool(),
            SqrtTool(),
            AbsTool(),
        ]


# ---------------------------------------------------------------------------
# MCP registration list
# ---------------------------------------------------------------------------

MCP_TOOLS: list[BaseTool] = [
    AddTool(),
    SubtractTool(),
    MultiplyTool(),
    DivideTool(),
    PowerTool(),
    ModuloTool(),
    SqrtTool(),
    AbsTool(),
]


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _fmt(value: float | int) -> str:
    """Format a numeric result as a clean string.

    Integer-valued floats are returned without a decimal point so that
    ``2.0`` becomes ``"2"`` rather than ``"2.0"``.
    """
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)
