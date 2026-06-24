"""
pymcpx.services.ipstack
-----------------------
MCP-compatible LangChain tools for the IPstack IP geolocation API.

Provides tools for:
- Single IP lookup via ``lookup_ip``
- Requester IP detection via ``lookup_requester_ip``
- Bulk IP lookup for up to 50 addresses via ``bulk_lookup_ip``
"""

from pymcpx.services.ipstack.SimulationEngine import (
    BulkLookupIPInput,
    IpstackSimulationEngine,
    LookupIPInput,
    LookupRequesterIPInput,
    bulk_lookup,
    lookup_ip,
    lookup_requester_ip,
)
from pymcpx.services.ipstack.tools import (
    MCP_TOOLS,
    BulkLookupIPTool,
    IpstackToolkit,
    LookupIPTool,
    LookupRequesterIPTool,
)

__all__ = [
    "MCP_TOOLS",
    "BulkLookupIPInput",
    "BulkLookupIPTool",
    "IpstackSimulationEngine",
    "IpstackToolkit",
    "LookupIPInput",
    "LookupIPTool",
    "LookupRequesterIPInput",
    "LookupRequesterIPTool",
    "bulk_lookup",
    "lookup_ip",
    "lookup_requester_ip",
]
