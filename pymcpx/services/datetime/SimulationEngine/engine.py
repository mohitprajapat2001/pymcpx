"""
DatetimeSimulationEngine — offline execution and simulation layer for the datetime service.
"""

from __future__ import annotations

from typing import Any

from pymcpx.services.datetime.SimulationEngine.models import (
    SimulatedResponse,
    SimulationCall,
)
from pymcpx.services.datetime.SimulationEngine.utils import inputs_match
from pymcpx.services.datetime.tools import (
    ConvertTimezoneTool,
    DatetimeToTimestampTool,
    GetCurrentTimeTool,
    GetDayOfWeekTool,
    TimestampToDatetimeTool,
)

_TOOL_REGISTRY: dict[str, Any] = {
    tool.name: tool
    for tool in [
        GetCurrentTimeTool(),
        ConvertTimezoneTool(),
        GetDayOfWeekTool(),
        TimestampToDatetimeTool(),
        DatetimeToTimestampTool(),
    ]
}


class DatetimeSimulationEngine:
    """Offline simulation engine for the datetime service."""

    def __init__(self) -> None:
        self._fixtures: list[SimulatedResponse] = []
        self.history: list[SimulationCall] = []

    def register(
        self,
        tool_name: str,
        output: str,
        input_match: dict[str, Any] | None = None,
    ) -> None:
        """Register a canned fixture response."""
        self._fixtures.append(
            SimulatedResponse(
                tool_name=tool_name,
                input_match=input_match or {},
                output=output,
            )
        )

    def run(self, tool_name: str, inputs: dict[str, Any] | None = None) -> str:
        """Run a datetime tool by name, checking fixtures first."""
        inputs = inputs or {}

        # Check registered fixtures first
        for fixture in self._fixtures:
            if fixture.tool_name == tool_name and inputs_match(inputs, fixture.input_match):
                call = SimulationCall(tool_name=tool_name, inputs=inputs, output=fixture.output)
                self.history.append(call)
                return fixture.output

        # Fall back to real tool execution
        tool = _TOOL_REGISTRY.get(tool_name)
        if tool is None:
            available = ", ".join(sorted(_TOOL_REGISTRY))
            raise ValueError(f"Unknown tool '{tool_name}'. Available tools: {available}")

        output: str = tool._run(**inputs)
        call = SimulationCall(tool_name=tool_name, inputs=inputs, output=output)
        self.history.append(call)
        return output

    def reset(self) -> None:
        """Clear call history and registered fixtures."""
        self._fixtures.clear()
        self.history.clear()

    @property
    def call_count(self) -> int:
        """Total number of run() calls recorded."""
        return len(self.history)

    def calls_for(self, tool_name: str) -> list[SimulationCall]:
        """Return all recorded calls for a specific tool."""
        return [c for c in self.history if c.tool_name == tool_name]

    @staticmethod
    def available_tools() -> list[str]:
        """Return sorted list of all registered tool names."""
        return sorted(_TOOL_REGISTRY)
