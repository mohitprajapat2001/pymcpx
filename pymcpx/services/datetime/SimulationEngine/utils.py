"""
Simulation utilities for the datetime service.
"""

from __future__ import annotations

from typing import Any


def inputs_match(candidate: dict[str, Any], input_match: dict[str, Any]) -> bool:
    """Return True when all key-value pairs in input_match appear in candidate."""
    return all(candidate.get(k) == v for k, v in input_match.items())


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge override into base and return a new dict."""
    result: dict[str, Any] = dict(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result
