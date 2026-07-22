from __future__ import annotations

from typing import Any

from pymcpx.services.zenserp.tools import (
    ZenserpBingSearchTool,
    ZenserpCountriesTool,
    ZenserpImageReverseSearchTool,
    ZenserpImageSearchTool,
    ZenserpLanguagesTool,
    ZenserpLocationsTool,
    ZenserpMapsSearchTool,
    ZenserpNewsSearchTool,
    ZenserpSearchEnginesTool,
    ZenserpSearchTool,
    ZenserpShoppingProductTool,
    ZenserpShoppingSearchTool,
    ZenserpStatusTool,
    ZenserpTrendingTool,
    ZenserpTrendsTool,
    ZenserpVideoSearchTool,
    ZenserpYandexSearchTool,
    ZenserpYouTubeSearchTool,
)

_TOOL_REGISTRY: dict[str, Any] = {
    tool.name: tool
    for tool in [
        ZenserpSearchTool(),
        ZenserpImageSearchTool(),
        ZenserpVideoSearchTool(),
        ZenserpNewsSearchTool(),
        ZenserpShoppingSearchTool(),
        ZenserpMapsSearchTool(),
        ZenserpImageReverseSearchTool(),
        ZenserpYouTubeSearchTool(),
        ZenserpBingSearchTool(),
        ZenserpYandexSearchTool(),
        ZenserpShoppingProductTool(),
        ZenserpTrendsTool(),
        ZenserpTrendingTool(),
        ZenserpStatusTool(),
        ZenserpLanguagesTool(),
        ZenserpCountriesTool(),
        ZenserpLocationsTool(),
        ZenserpSearchEnginesTool(),
    ]
}


class ZenserpSimulationEngine:
    """Offline simulation engine for the Zenserp service."""

    def __init__(self) -> None:
        self._fixtures: list[dict[str, Any]] = []
        self.history: list[dict[str, Any]] = []

    def register(
        self,
        tool_name: str,
        output: str,
        input_match: dict[str, Any] | None = None,
    ) -> None:
        self._fixtures.append(
            {
                "tool_name": tool_name,
                "input_match": input_match or {},
                "output": output,
            }
        )

    def run(self, tool_name: str, inputs: dict[str, Any] | None = None) -> str:
        inputs = inputs or {}

        for fixture in self._fixtures:
            if fixture["tool_name"] == tool_name and _inputs_match(inputs, fixture["input_match"]):
                call = {"tool_name": tool_name, "inputs": inputs, "output": fixture["output"]}
                self.history.append(call)
                return fixture["output"]

        tool = _TOOL_REGISTRY.get(tool_name)
        if tool is None:
            available = ", ".join(sorted(_TOOL_REGISTRY))
            raise ValueError(f"Unknown tool '{tool_name}'. Available tools: {available}")

        output: str = tool._run(**inputs)
        call = {"tool_name": tool_name, "inputs": inputs, "output": output}
        self.history.append(call)
        return output

    def reset(self) -> None:
        self._fixtures.clear()
        self.history.clear()

    @property
    def call_count(self) -> int:
        return len(self.history)

    def calls_for(self, tool_name: str) -> list[dict[str, Any]]:
        return [c for c in self.history if c["tool_name"] == tool_name]

    @staticmethod
    def available_tools() -> list[str]:
        return sorted(_TOOL_REGISTRY)


def _inputs_match(candidate: dict[str, Any], match: dict[str, Any]) -> bool:
    return all(candidate.get(k) == v for k, v in match.items())
