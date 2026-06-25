"""
LangChain BaseTool subclasses for the Numverify service.
"""

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from pymcpx.services.numverify.SimulationEngine.models import (
    NumverifyCountriesInput,
    NumverifyValidateInput,
)
from pymcpx.services.numverify.SimulationEngine.utils import (
    get_supported_countries,
    validate_phone_number,
)


class NumverifyValidateTool(BaseTool):
    """Validate a phone number and return its carrier, location, line type."""

    name: str = "numverify_validate"
    description: str = (
        "Validate a phone number and return detailed information including "
        "validity, local and international formats, country, location, "
        "carrier, and line type (mobile, landline, VoIP)."
    )
    args_schema: type[BaseModel] = NumverifyValidateInput

    def _run(
        self,
        number: str,
        country_code: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return validate_phone_number(number=number, country_code=country_code)
        except Exception as exc:
            return f"Error: {exc}"


class NumverifyCountriesTool(BaseTool):
    """List all supported countries with their dialing codes."""

    name: str = "numverify_countries"
    description: str = (
        "List all 232 countries and territories supported by the Numverify "
        "API, including their ISO codes and international dialing codes."
    )
    args_schema: type[BaseModel] = NumverifyCountriesInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_supported_countries()
        except Exception as exc:
            return f"Error: {exc}"


class NumverifyToolkit:
    """Convenience bundle that exposes all numverify tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every numverify tool instance."""
        return [
            NumverifyValidateTool(),
            NumverifyCountriesTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    NumverifyValidateTool(),
    NumverifyCountriesTool(),
]
