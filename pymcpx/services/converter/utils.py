"""
Utility helpers for the converter service containing conversion logic and scales.
"""

from __future__ import annotations

# Conversion factors to base unit (meters)
LENGTH_FACTORS: dict[str, float] = {
    "m": 1.0,
    "meter": 1.0,
    "meters": 1.0,
    "cm": 0.01,
    "centimeter": 0.01,
    "centimeters": 0.01,
    "mm": 0.001,
    "millimeter": 0.001,
    "millimeters": 0.001,
    "km": 1000.0,
    "kilometer": 1000.0,
    "kilometers": 1000.0,
    "inch": 0.0254,
    "inches": 0.0254,
    "in": 0.0254,
    "ft": 0.3048,
    "foot": 0.3048,
    "feet": 0.3048,
    "yard": 0.9144,
    "yards": 0.9144,
    "yd": 0.9144,
    "mile": 1609.344,
    "miles": 1609.344,
    "mi": 1609.344,
}

# Conversion factors to base unit (kilograms)
WEIGHT_FACTORS: dict[str, float] = {
    "kg": 1.0,
    "kilogram": 1.0,
    "kilograms": 1.0,
    "g": 0.001,
    "gram": 0.001,
    "grams": 0.001,
    "mg": 0.000001,
    "milligram": 0.000001,
    "milligrams": 0.000001,
    "lb": 0.45359237,
    "pound": 0.45359237,
    "pounds": 0.45359237,
    "oz": 0.028349523125,
    "ounce": 0.028349523125,
    "ounces": 0.028349523125,
}


def convert_length_units(value: float, from_unit: str, to_unit: str) -> float:
    """Convert length from one unit to another."""
    from_u = from_unit.strip().lower()
    to_u = to_unit.strip().lower()

    if from_u not in LENGTH_FACTORS:
        raise ValueError(
            f"Unsupported length unit '{from_unit}'. "
            f"Supported: {sorted(set(LENGTH_FACTORS.keys()))}"
        )
    if to_u not in LENGTH_FACTORS:
        raise ValueError(
            f"Unsupported length unit '{to_unit}'. Supported: {sorted(set(LENGTH_FACTORS.keys()))}"
        )

    # Convert to base (meters) then to target unit
    val_in_meters = value * LENGTH_FACTORS[from_u]
    return val_in_meters / LENGTH_FACTORS[to_u]


def convert_weight_units(value: float, from_unit: str, to_unit: str) -> float:
    """Convert weight from one unit to another."""
    from_u = from_unit.strip().lower()
    to_u = to_unit.strip().lower()

    if from_u not in WEIGHT_FACTORS:
        raise ValueError(
            f"Unsupported weight unit '{from_unit}'. "
            f"Supported: {sorted(set(WEIGHT_FACTORS.keys()))}"
        )
    if to_u not in WEIGHT_FACTORS:
        raise ValueError(
            f"Unsupported weight unit '{to_unit}'. Supported: {sorted(set(WEIGHT_FACTORS.keys()))}"
        )

    # Convert to base (kilograms) then to target unit
    val_in_kg = value * WEIGHT_FACTORS[from_u]
    return val_in_kg / WEIGHT_FACTORS[to_u]


def convert_temp_units(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature from one unit to another."""
    from_u = from_unit.strip().lower()
    to_u = to_unit.strip().lower()

    # Normalize names
    alias_map = {
        "c": "celsius",
        "celsius": "celsius",
        "f": "fahrenheit",
        "fahrenheit": "fahrenheit",
        "k": "kelvin",
        "kelvin": "kelvin",
    }

    if from_u not in alias_map:
        raise ValueError(f"Unsupported temperature unit '{from_unit}'. Supported: c, f, k.")
    if to_u not in alias_map:
        raise ValueError(f"Unsupported temperature unit '{to_unit}'. Supported: c, f, k.")

    norm_from = alias_map[from_u]
    norm_to = alias_map[to_u]

    if norm_from == norm_to:
        return value

    # Convert to Celsius first
    if norm_from == "celsius":
        val_in_c = value
    elif norm_from == "fahrenheit":
        val_in_c = (value - 32) * 5 / 9
    else:  # kelvin
        val_in_c = value - 273.15

    # Convert Celsius to target
    if norm_to == "celsius":
        return val_in_c
    elif norm_to == "fahrenheit":
        return (val_in_c * 9 / 5) + 32
    else:  # kelvin
        return val_in_c + 273.15
