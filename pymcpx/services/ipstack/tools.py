"""
LangChain BaseTool implementations for the IPstack IP geolocation service.
"""

from __future__ import annotations

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from pymcpx.services.ipstack.SimulationEngine.models import (
    BulkLookupIPInput,
    LookupIPInput,
    LookupRequesterIPInput,
)
from pymcpx.services.ipstack.SimulationEngine.utils import (
    bulk_lookup,
    lookup_ip,
    lookup_requester_ip,
)


class LookupIPTool(BaseTool):
    """Look up geolocation data for a single IPv4 or IPv6 address."""

    name: str = "lookup_ip"
    description: str = (
        "Look up detailed geolocation data for a single IPv4 or IPv6 address. "
        "Returns location data including country, region, city, coordinates, "
        "timezone, currency, connection info, and optional security insights."
    )
    args_schema: type[BaseModel] = LookupIPInput

    def _run(
        self,
        ip_address: str,
        fields: str | None = None,
        hostname: int | None = None,
        security: int | None = None,
        language: str | None = None,
        output: str | None = None,
        callback: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return lookup_ip(ip_address, fields, hostname, security, language, output, callback)
        except Exception as exc:
            return f"Error: {exc}"


class LookupRequesterIPTool(BaseTool):
    """Detect and return geolocation for the requester's own IP address."""

    name: str = "lookup_requester_ip"
    description: str = (
        "Detect and return geolocation data for the requester's own IP address. "
        "Returns country, region, city, coordinates, and more."
    )
    args_schema: type[BaseModel] = LookupRequesterIPInput

    def _run(
        self,
        fields: str | None = None,
        hostname: int | None = None,
        security: int | None = None,
        language: str | None = None,
        output: str | None = None,
        callback: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return lookup_requester_ip(fields, hostname, security, language, output, callback)
        except Exception as exc:
            return f"Error: {exc}"


class BulkLookupIPTool(BaseTool):
    """Look up geolocation data for multiple IP addresses at once."""

    name: str = "bulk_lookup_ip"
    description: str = (
        "Look up geolocation data for multiple IPv4 or IPv6 addresses at once. "
        "Provide up to 50 comma-separated IP addresses."
    )
    args_schema: type[BaseModel] = BulkLookupIPInput

    def _run(
        self,
        ip_addresses: str,
        fields: str | None = None,
        hostname: int | None = None,
        security: int | None = None,
        language: str | None = None,
        output: str | None = None,
        callback: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return bulk_lookup(ip_addresses, fields, hostname, security, language, output, callback)
        except Exception as exc:
            return f"Error: {exc}"


class IpstackToolkit:
    """Convenience bundle that exposes all IPstack tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every IPstack tool instance."""
        return [
            LookupIPTool(),
            LookupRequesterIPTool(),
            BulkLookupIPTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    LookupIPTool(),
    LookupRequesterIPTool(),
    BulkLookupIPTool(),
]
