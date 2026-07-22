"""
Pydantic input models for the ebird service tools.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GetRecentObservationsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """Input schema for get_recent_observations tool."""

    region_code: str = Field(
        description="Country, state, county, or location code (e.g. US, US-NY, US-NY-103)."
    )
    back: int | None = Field(
        default=None, ge=1, le=30, description="Number of days back to fetch observations (1-30)."
    )
    hotspot: bool | None = Field(default=None, description="Only fetch observations from hotspots.")
    include_provisional: bool | None = Field(
        default=None, description="Include unreviewed observations.", alias="includeProvisional"
    )
    max_results: int | None = Field(
        default=50,
        ge=1,
        le=200,
        description="Maximum number of observations to return (max 200).",
        alias="maxResults",
    )
    spp_locale: str | None = Field(
        default=None,
        description="Language for species common names (e.g. en, fr).",
        alias="sppLocale",
    )


class GetRecentSpeciesObservationsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """Input schema for get_recent_species_observations tool."""

    region_code: str = Field(description="Country, state, county, or location code.")
    species_code: str = Field(description="eBird species code (e.g. houfin).")
    back: int | None = Field(default=None, ge=1, le=30, description="Number of days back (1-30).")
    max_results: int | None = Field(
        default=50, ge=1, le=200, description="Maximum observations (max 200).", alias="maxResults"
    )


class GetNearbyObservationsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """Input schema for get_nearby_observations tool."""

    species_code: str = Field(description="eBird species code (e.g. houfin).")
    lat: float = Field(description="Latitude of the location.")
    lng: float = Field(description="Longitude of the location.")
    max_results: int | None = Field(
        default=50, ge=1, le=200, description="Maximum observations (max 200).", alias="maxResults"
    )


class GetHotspotsInput(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    """Input schema for get_hotspots tool."""

    region_code: str = Field(description="Country, state, county, or location code.")
    back: int | None = Field(default=None, ge=1, le=30, description="Number of days back (1-30).")
    max_results: int | None = Field(
        default=50, ge=1, le=200, description="Maximum hotspots (max 200).", alias="maxResults"
    )


class GetTaxonomyInput(BaseModel):
    """Input schema for get_taxonomy tool."""

    cat: str | None = Field(
        default=None, description="Taxonomic category filter (e.g. species, ebird)."
    )
    search: str | None = Field(
        default=None,
        description="Fuzzy search term to match against species common or scientific names.",
    )
    limit: int = Field(default=50, ge=1, le=200, description="Maximum number of results (max 200).")


class GetSpeciesListInput(BaseModel):
    """Input schema for get_species_list tool."""

    region_code: str = Field(description="Country, state, county, or location code.")
    search: str | None = Field(
        default=None, description="Fuzzy search term to match against species names."
    )
    limit: int = Field(default=50, ge=1, le=200, description="Maximum number of results (max 200).")
