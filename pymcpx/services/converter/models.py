"""
Pydantic input models for the converter service tools.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class LengthConversionInput(BaseModel):
    """Input schema for convert_length tool."""

    value: float = Field(description="The numeric value to convert.")
    from_unit: str = Field(
        description="Source length unit (e.g. m, cm, mm, km, inch, ft, yard, mile)."
    )
    to_unit: str = Field(
        description="Target length unit (e.g. m, cm, mm, km, inch, ft, yard, mile)."
    )


class WeightConversionInput(BaseModel):
    """Input schema for convert_weight tool."""

    value: float = Field(description="The numeric value to convert.")
    from_unit: str = Field(
        description="The source unit of weight (e.g., 'kg', 'g', 'mg', 'lb', 'oz')."
    )
    to_unit: str = Field(
        description="The target unit of weight (e.g., 'kg', 'g', 'mg', 'lb', 'oz')."
    )


class TemperatureConversionInput(BaseModel):
    """Input schema for convert_temperature tool."""

    value: float = Field(description="The numeric value to convert.")
    from_unit: str = Field(
        description="Source temp unit ('c', 'f', 'k', 'celsius', 'fahrenheit', 'kelvin')."
    )
    to_unit: str = Field(
        description="Target temp unit ('c', 'f', 'k', 'celsius', 'fahrenheit', 'kelvin')."
    )
