"""
LangChain BaseTool implementations for the ebird service.
"""

from __future__ import annotations

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel  # noqa: TC002

from pymcpx.services.ebird.SimulationEngine.models import (
    GetHotspotsInput,
    GetNearbyObservationsInput,
    GetRecentObservationsInput,
    GetRecentSpeciesObservationsInput,
    GetSpeciesListInput,
    GetTaxonomyInput,
)
from pymcpx.services.ebird.SimulationEngine.utils import (
    get_hotspots,
    get_nearby_observations,
    get_recent_observations,
    get_recent_species_observations,
    get_species_list,
    get_taxonomy,
)


class GetRecentObservationsTool(BaseTool):
    """Get recent bird observations in a region."""

    name: str = "get_recent_observations"
    description: str = (
        "Get the list of recent bird observations (up to 30 days) "
        "seen in a country, state, county, or location. "
        "Results are limited to avoid overwhelming output."
    )
    args_schema: type[BaseModel] = GetRecentObservationsInput

    def _run(
        self,
        region_code: str,
        back: int | None = None,
        hotspot: bool | None = None,
        include_provisional: bool | None = None,
        max_results: int | None = 50,
        spp_locale: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_recent_observations(
                region_code, back, hotspot, include_provisional, max_results, spp_locale
            )
        except Exception as exc:
            return f"Error: {exc}"


class GetRecentSpeciesObservationsTool(BaseTool):
    """Get recent observations of a specific species in a region."""

    name: str = "get_recent_species_observations"
    description: str = (
        "Get recent observations of a specific bird species in a region. "
        "Results are limited to avoid overwhelming output."
    )
    args_schema: type[BaseModel] = GetRecentSpeciesObservationsInput

    def _run(
        self,
        region_code: str,
        species_code: str,
        back: int | None = None,
        max_results: int | None = 50,
        **kwargs: Any,
    ) -> str:
        try:
            return get_recent_species_observations(region_code, species_code, back, max_results)
        except Exception as exc:
            return f"Error: {exc}"


class GetNearbyObservationsTool(BaseTool):
    """Get nearest observations of a species."""

    name: str = "get_nearby_observations"
    description: str = (
        "Get the nearest observations of a bird species within 50km "
        "of a given latitude and longitude. "
        "Results are limited to avoid overwhelming output."
    )
    args_schema: type[BaseModel] = GetNearbyObservationsInput

    def _run(
        self,
        species_code: str,
        lat: float,
        lng: float,
        max_results: int | None = 50,
        **kwargs: Any,
    ) -> str:
        try:
            return get_nearby_observations(species_code, lat, lng, max_results)
        except Exception as exc:
            return f"Error: {exc}"


class GetHotspotsTool(BaseTool):
    """Get birding hotspots in a region."""

    name: str = "get_hotspots"
    description: str = (
        "Get birding hotspots in a country, state, or county. "
        "Results are limited to avoid overwhelming output."
    )
    args_schema: type[BaseModel] = GetHotspotsInput

    def _run(
        self,
        region_code: str,
        back: int | None = None,
        max_results: int | None = 50,
        **kwargs: Any,
    ) -> str:
        try:
            return get_hotspots(region_code, back, max_results)
        except Exception as exc:
            return f"Error: {exc}"


class GetTaxonomyTool(BaseTool):
    """Get eBird taxonomy with optional fuzzy search."""

    name: str = "get_taxonomy"
    description: str = (
        "Get the eBird taxonomy / species list. "
        "Optionally filter by taxonomic category or provide a search term "
        "to fuzzy-match against common and scientific names. "
        "Results are limited to avoid overwhelming output."
    )
    args_schema: type[BaseModel] = GetTaxonomyInput

    def _run(
        self,
        limit: int = 50,
        cat: str | None = None,
        search: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_taxonomy(cat, search, limit)
        except Exception as exc:
            return f"Error: {exc}"


class GetSpeciesListTool(BaseTool):
    """Get species list for a region with optional fuzzy search."""

    name: str = "get_species_list"
    description: str = (
        "Get the list of bird species recorded in a region. "
        "Provide a search term to fuzzy-match against species names. "
        "Results are limited to avoid overwhelming output."
    )
    args_schema: type[BaseModel] = GetSpeciesListInput

    def _run(
        self,
        region_code: str,
        limit: int = 50,
        search: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_species_list(region_code, search, limit)
        except Exception as exc:
            return f"Error: {exc}"


class EbirdToolkit:
    """Convenience bundle that exposes all ebird tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every ebird tool instance."""
        return [
            GetRecentObservationsTool(),
            GetRecentSpeciesObservationsTool(),
            GetNearbyObservationsTool(),
            GetHotspotsTool(),
            GetTaxonomyTool(),
            GetSpeciesListTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    GetRecentObservationsTool(),
    GetRecentSpeciesObservationsTool(),
    GetNearbyObservationsTool(),
    GetHotspotsTool(),
    GetTaxonomyTool(),
    GetSpeciesListTool(),
]
