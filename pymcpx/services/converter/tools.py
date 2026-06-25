"""
LangChain BaseTool subclasses for unit conversion tools.
"""

from __future__ import annotations

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from pymcpx.services.converter.models import (
    LengthConversionInput,
    TemperatureConversionInput,
    WeightConversionInput,
)
from pymcpx.services.converter.utils import (
    convert_length_units,
    convert_temp_units,
    convert_weight_units,
)


class ConvertLengthTool(BaseTool):
    """Convert length from one unit to another."""

    name: str = "convert_length"
    description: str = (
        "Convert a length value to another unit (e.g. m, cm, mm, km, inch, ft, yard, mile)."
    )
    args_schema: type[BaseModel] = LengthConversionInput

    def _run(self, value: float, from_unit: str, to_unit: str, **kwargs: Any) -> str:
        try:
            res = convert_length_units(value, from_unit, to_unit)
            return _fmt(res)
        except Exception as exc:
            return f"Error: {exc}"


class ConvertWeightTool(BaseTool):
    """Convert weight from one unit to another."""

    name: str = "convert_weight"
    description: str = "Convert a weight value from one unit to another (e.g. kg, g, mg, lb, oz)."
    args_schema: type[BaseModel] = WeightConversionInput

    def _run(self, value: float, from_unit: str, to_unit: str, **kwargs: Any) -> str:
        try:
            res = convert_weight_units(value, from_unit, to_unit)
            return _fmt(res)
        except Exception as exc:
            return f"Error: {exc}"


class ConvertTemperatureTool(BaseTool):
    """Convert temperature from one unit to another."""

    name: str = "convert_temperature"
    description: str = (
        "Convert a temperature value from one unit to another (e.g. Celsius, Fahrenheit, Kelvin)."
    )
    args_schema: type[BaseModel] = TemperatureConversionInput

    def _run(self, value: float, from_unit: str, to_unit: str, **kwargs: Any) -> str:
        try:
            res = convert_temp_units(value, from_unit, to_unit)
            return _fmt(res)
        except Exception as exc:
            return f"Error: {exc}"


class ConverterToolkit:
    """Convenience bundle that exposes all converter tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every converter tool instance."""
        return [
            ConvertLengthTool(),
            ConvertWeightTool(),
            ConvertTemperatureTool(),
        ]


# ---------------------------------------------------------------------------
# MCP registration list
# ---------------------------------------------------------------------------

MCP_TOOLS: list[BaseTool] = [
    ConvertLengthTool(),
    ConvertWeightTool(),
    ConvertTemperatureTool(),
]


def _fmt(value: float) -> str:
    """Format a float result to drop trailing decimal places if it's integer-equivalent."""
    if value.is_integer():
        return str(int(value))
    # Round to 6 decimal places to prevent float precision noise
    rounded = round(value, 6)
    if rounded.is_integer():
        return str(int(rounded))
    return str(rounded)
