"""
Simulation models for the converter service.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class SimulationCall(BaseModel):
    """A single recorded invocation of a converter tool via the engine."""

    tool_name: str = Field(description="The MCP tool name that was invoked.")
    inputs: dict[str, Any] = Field(
        default_factory=dict,
        description="The raw input dict passed to the engine.",
    )
    output: str = Field(description="The string result returned by the tool.")

    model_config = {"frozen": True}


class SimulatedResponse(BaseModel):
    """A fixture entry: when *tool_name* is called with inputs matching
    *input_match*, return *output* verbatim instead of running the real tool.
    """

    tool_name: str = Field(description="MCP tool name this fixture applies to.")
    input_match: dict[str, Any] = Field(
        default_factory=dict,
        description=(
            "Key-value pairs that must all be present (and equal) in the "
            "caller's inputs for this fixture to fire. Empty dict matches any input."
        ),
    )
    output: str = Field(description="The canned string to return when matched.")

    model_config = {"frozen": True}
