"""
LangChain BaseTool implementations for the catfacts service.
"""

from __future__ import annotations

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel  # noqa: TC002

from pymcpx.services.catfacts.SimulationEngine.models import (
    GetBreedsInput,
    GetFactsInput,
    GetRandomFactInput,
)
from pymcpx.services.catfacts.SimulationEngine.utils import (
    get_breeds,
    get_facts,
    get_random_fact,
)


class GetBreedsTool(BaseTool):
    """Fetch a list of cat breeds."""

    name: str = "get_breeds"
    description: str = (
        "Fetch a list of cat breeds from the Cat Fact API. "
        "Returns breed name, country, origin, coat, and pattern for each breed."
    )
    args_schema: type[BaseModel] = GetBreedsInput

    def _run(
        self,
        limit: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_breeds(limit)
        except Exception as exc:
            return f"Error: {exc}"


class GetRandomFactTool(BaseTool):
    """Fetch a random cat fact."""

    name: str = "get_random_fact"
    description: str = (
        "Fetch a random cat fact from the Cat Fact API. "
        "Optionally limit the maximum length of the returned fact."
    )
    args_schema: type[BaseModel] = GetRandomFactInput

    def _run(
        self,
        max_length: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_random_fact(max_length)
        except Exception as exc:
            return f"Error: {exc}"


class GetFactsTool(BaseTool):
    """Fetch a list of cat facts."""

    name: str = "get_facts"
    description: str = (
        "Fetch a list of cat facts from the Cat Fact API. "
        "Optionally limit the maximum length of each fact and the number of facts returned."
    )
    args_schema: type[BaseModel] = GetFactsInput

    def _run(
        self,
        max_length: int | None = None,
        limit: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_facts(max_length, limit)
        except Exception as exc:
            return f"Error: {exc}"


class CatfactsToolkit:
    """Convenience bundle that exposes all catfacts tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every catfacts tool instance."""
        return [
            GetBreedsTool(),
            GetRandomFactTool(),
            GetFactsTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    GetBreedsTool(),
    GetRandomFactTool(),
    GetFactsTool(),
]
