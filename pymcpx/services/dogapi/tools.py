"""
LangChain BaseTool implementations for the dogapi service.
"""

from __future__ import annotations

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel  # noqa: TC002

from pymcpx.services.dogapi.SimulationEngine.models import (
    GetRandomDogImageByBreedInput,
    GetRandomDogImageInput,
    ListBreedsInput,
)
from pymcpx.services.dogapi.SimulationEngine.utils import (
    get_random_dog_image,
    get_random_dog_image_by_breed,
    list_breeds,
)


class ListBreedsTool(BaseTool):
    """List all dog breeds with optional fuzzy search."""

    name: str = "list_breeds"
    description: str = (
        "List all available dog breeds from the Dog CEO API. "
        "If a search term is provided, fuzzy-matches against all breed names "
        "and returns the best matches. Results are limited to avoid overwhelming output."
    )
    args_schema: type[BaseModel] = ListBreedsInput

    def _run(
        self,
        limit: int = 20,
        search: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return list_breeds(search, limit)
        except Exception as exc:
            return f"Error: {exc}"


class GetRandomDogImageTool(BaseTool):
    """Get a random dog image URL."""

    name: str = "get_random_dog_image"
    description: str = "Get a random dog image URL from the Dog CEO API."
    args_schema: type[BaseModel] = GetRandomDogImageInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_random_dog_image()
        except Exception as exc:
            return f"Error: {exc}"


class GetRandomDogImageByBreedTool(BaseTool):
    """Get a random dog image URL for a specific breed."""

    name: str = "get_random_dog_image_by_breed"
    description: str = (
        "Get a random dog image URL for a specific breed. "
        "Use list_breeds first to find the exact breed name."
    )
    args_schema: type[BaseModel] = GetRandomDogImageByBreedInput

    def _run(
        self,
        breed: str,
        **kwargs: Any,
    ) -> str:
        try:
            return get_random_dog_image_by_breed(breed)
        except Exception as exc:
            return f"Error: {exc}"


class DogapiToolkit:
    """Convenience bundle that exposes all dogapi tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every dogapi tool instance."""
        return [
            ListBreedsTool(),
            GetRandomDogImageTool(),
            GetRandomDogImageByBreedTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    ListBreedsTool(),
    GetRandomDogImageTool(),
    GetRandomDogImageByBreedTool(),
]
