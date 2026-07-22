"""
pymcpx.services.ebird
---------------------
MCP-compatible LangChain tools for the eBird API.

Provides tools for:
- Getting recent bird observations in a region via ``get_recent_observations``
- Getting recent observations of a specific species via ``get_recent_species_observations``
- Getting nearby observations of a species via ``get_nearby_observations``
- Getting birding hotspots via ``get_hotspots``
- Getting eBird taxonomy via ``get_taxonomy``
- Getting species list for a region via ``get_species_list``
"""

from pymcpx.services.ebird.SimulationEngine import (
    EbirdSimulationEngine,
    GetHotspotsInput,
    GetNearbyObservationsInput,
    GetRecentObservationsInput,
    GetRecentSpeciesObservationsInput,
    GetSpeciesListInput,
    GetTaxonomyInput,
)
from pymcpx.services.ebird.tools import (
    MCP_TOOLS,
    EbirdToolkit,
    GetHotspotsTool,
    GetNearbyObservationsTool,
    GetRecentObservationsTool,
    GetRecentSpeciesObservationsTool,
    GetSpeciesListTool,
    GetTaxonomyTool,
)

__all__ = [
    "MCP_TOOLS",
    "EbirdSimulationEngine",
    "EbirdToolkit",
    "GetHotspotsInput",
    "GetHotspotsTool",
    "GetNearbyObservationsInput",
    "GetNearbyObservationsTool",
    "GetRecentObservationsInput",
    "GetRecentObservationsTool",
    "GetRecentSpeciesObservationsInput",
    "GetRecentSpeciesObservationsTool",
    "GetSpeciesListInput",
    "GetSpeciesListTool",
    "GetTaxonomyInput",
    "GetTaxonomyTool",
]
