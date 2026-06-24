"""
Pydantic input models for the IPstack service tools.
"""

from pydantic import BaseModel, Field


class LookupIPInput(BaseModel):
    """Input schema for lookup_ip tool."""

    ip_address: str = Field(description="IPv4 or IPv6 address to look up.")
    security: int = Field(
        default=1,
        description="Set to 1 to enable security insights (proxy, crawler, Tor, threat level).",
    )
    hostname: int = Field(default=0, description="Set to 1 to enable hostname lookup.")
    fields: str | None = Field(
        default=None,
        description="Comma-separated response fields to return (e.g. 'country_code,city').",
    )
    language: str | None = Field(
        default=None,
        description="2-letter language code for localized response data.",
    )
    output: str | None = Field(
        default=None,
        description="Response format ('json' or 'xml'). Defaults to 'json'.",
    )
    callback: str | None = Field(
        default=None,
        description="JavaScript function name for JSONP wrapping.",
    )


class LookupRequesterIPInput(BaseModel):
    """Input schema for lookup_requester_ip tool."""

    security: int = Field(
        default=0,
        description="Set to 1 to include security insights.",
    )
    hostname: int = Field(default=0, description="Set to 1 to include the resolved hostname.")
    fields: str | None = Field(
        default=None,
        description="Comma-separated response fields to return.",
    )
    language: str | None = Field(
        default=None,
        description="2-letter language code for localized response.",
    )
    output: str | None = Field(
        default=None,
        description="Response format ('json' or 'xml').",
    )
    callback: str | None = Field(
        default=None,
        description="JavaScript function name for JSONP wrapping.",
    )


class BulkLookupIPInput(BaseModel):
    """Input schema for bulk_lookup_ip tool."""

    ip_addresses: str = Field(
        description="Comma-separated list of up to 50 IP addresses to look up."
    )
    security: int = Field(
        default=0,
        description="Set to 1 to include security insights.",
    )
    hostname: int = Field(default=0, description="Set to 1 to include hostname lookup.")
    fields: str | None = Field(
        default=None,
        description="Comma-separated response fields to return.",
    )
    language: str | None = Field(
        default=None,
        description="2-letter language code for localized response.",
    )
    output: str | None = Field(
        default=None,
        description="Response format ('json' or 'xml').",
    )
    callback: str | None = Field(
        default=None,
        description="JavaScript function name for JSONP wrapping.",
    )
