"""
LangChain BaseTool implementations for the cataas service.
"""

from __future__ import annotations

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel  # noqa: TC002

from pymcpx.services.cataas.SimulationEngine.models import (
    CountCatsInput,
    GetCatByIdInput,
    GetCatByIdSayingInput,
    GetCatByTagInput,
    GetRandomCatByTagSayingInput,
    GetRandomCatInput,
    GetRandomCatSayingInput,
    ListCatsInput,
    ListTagsInput,
)
from pymcpx.services.cataas.SimulationEngine.utils import (
    _get_cat_response,
    count_cats,
    list_cats,
    list_tags,
)


class ListTagsTool(BaseTool):
    """List all available tags with optional fuzzy search."""

    name: str = "list_tags"
    description: str = (
        "List available cat tags from CATAAS. "
        "If a search term is provided, fuzzy-matches against all available tags "
        "and returns the best matches. Results are limited to avoid overwhelming output."
    )
    args_schema: type[BaseModel] = ListTagsInput

    def _run(
        self,
        limit: int = 20,
        search: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return list_tags(search, limit)
        except Exception as exc:
            return f"Error: {exc}"


class ListCatsTool(BaseTool):
    """List cats with optional tag filtering and fuzzy search."""

    name: str = "list_cats"
    description: str = (
        "List cats from CATAAS. "
        "Supports filtering by comma-separated tags, or provide a search term "
        "to fuzzy-match against available tags and auto-filter. "
        "Results are limited to avoid overwhelming output."
    )
    args_schema: type[BaseModel] = ListCatsInput

    def _run(
        self,
        limit: int = 10,
        skip: int = 0,
        tags: str | None = None,
        search: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return list_cats(limit, skip, tags, search)
        except Exception as exc:
            return f"Error: {exc}"


class CountCatsTool(BaseTool):
    """Count all cats in the CATAAS database."""

    name: str = "count_cats"
    description: str = "Count how many cats are in the CATAAS database."
    args_schema: type[BaseModel] = CountCatsInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return count_cats()
        except Exception as exc:
            return f"Error: {exc}"


class GetRandomCatTool(BaseTool):
    """Get a random cat image URL or metadata."""

    name: str = "get_random_cat"
    description: str = (
        "Get a random cat from CATAAS. "
        "Returns an image URL by default. Set json=true to get JSON metadata instead. "
        "Supports image transformation options: type, filter, fit, position, width, height, blur, "
        "r/g/b (custom filter colors), brightness, saturation, hue, lightness, html."
    )
    args_schema: type[BaseModel] = GetRandomCatInput

    def _run(self, **kwargs: Any) -> str:
        try:
            params = GetRandomCatInput(**kwargs)
            return _get_cat_response("/cat", params)
        except Exception as exc:
            return f"Error: {exc}"


class GetCatByIdTool(BaseTool):
    """Get a cat by its ID."""

    name: str = "get_cat_by_id"
    description: str = (
        "Get a cat image by its CATAAS ID. "
        "Returns an image URL by default. Set json=true to get JSON metadata instead."
    )
    args_schema: type[BaseModel] = GetCatByIdInput

    def _run(self, **kwargs: Any) -> str:
        try:
            params = GetCatByIdInput(**kwargs)
            return _get_cat_response(f"/cat/{params.id}", params)
        except Exception as exc:
            return f"Error: {exc}"


class GetCatByTagTool(BaseTool):
    """Get a random cat by tag."""

    name: str = "get_cat_by_tag"
    description: str = (
        "Get a random cat image filtered by tag. "
        "Returns an image URL by default. Set json=true to get JSON metadata instead."
    )
    args_schema: type[BaseModel] = GetCatByTagInput

    def _run(self, **kwargs: Any) -> str:
        try:
            params = GetCatByTagInput(**kwargs)
            return _get_cat_response(f"/cat/{params.tag}", params)
        except Exception as exc:
            return f"Error: {exc}"


class GetRandomCatSayingTool(BaseTool):
    """Get a random cat saying text."""

    name: str = "get_random_cat_saying"
    description: str = (
        "Get a random cat image with text overlaid. "
        "Returns an image URL by default. Set json=true to get JSON metadata instead. "
        "Text overlay options: font, font_size, font_color, font_background."
    )
    args_schema: type[BaseModel] = GetRandomCatSayingInput

    def _run(self, **kwargs: Any) -> str:
        try:
            params = GetRandomCatSayingInput(**kwargs)
            return _get_cat_response(f"/cat/says/{params.text}", params)
        except Exception as exc:
            return f"Error: {exc}"


class GetCatByIdSayingTool(BaseTool):
    """Get a cat by ID saying text."""

    name: str = "get_cat_by_id_saying"
    description: str = (
        "Get a cat image by ID with text overlaid. "
        "Returns an image URL by default. Set json=true to get JSON metadata instead."
    )
    args_schema: type[BaseModel] = GetCatByIdSayingInput

    def _run(self, **kwargs: Any) -> str:
        try:
            params = GetCatByIdSayingInput(**kwargs)
            return _get_cat_response(f"/cat/{params.id}/says/{params.text}", params)
        except Exception as exc:
            return f"Error: {exc}"


class GetRandomCatByTagSayingTool(BaseTool):
    """Get a random cat by tag saying text."""

    name: str = "get_random_cat_by_tag_saying"
    description: str = (
        "Get a random cat image filtered by tag with text overlaid. "
        "Returns an image URL by default. Set json=true to get JSON metadata instead."
    )
    args_schema: type[BaseModel] = GetRandomCatByTagSayingInput

    def _run(self, **kwargs: Any) -> str:
        try:
            params = GetRandomCatByTagSayingInput(**kwargs)
            return _get_cat_response(f"/cat/{params.tag}/says/{params.text}", params)
        except Exception as exc:
            return f"Error: {exc}"


class CataasToolkit:
    """Convenience bundle that exposes all cataas tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every cataas tool instance."""
        return [
            ListTagsTool(),
            ListCatsTool(),
            CountCatsTool(),
            GetRandomCatTool(),
            GetCatByIdTool(),
            GetCatByTagTool(),
            GetRandomCatSayingTool(),
            GetCatByIdSayingTool(),
            GetRandomCatByTagSayingTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    ListTagsTool(),
    ListCatsTool(),
    CountCatsTool(),
    GetRandomCatTool(),
    GetCatByIdTool(),
    GetCatByTagTool(),
    GetRandomCatSayingTool(),
    GetCatByIdSayingTool(),
    GetRandomCatByTagSayingTool(),
]
