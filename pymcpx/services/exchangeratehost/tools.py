from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from pymcpx.services.exchangeratehost.SimulationEngine.models import (
    ExchangeratehostChangeInput,
    ExchangeratehostConvertInput,
    ExchangeratehostHistoricalInput,
    ExchangeratehostLiveInput,
    ExchangeratehostTimeframeInput,
)
from pymcpx.services.exchangeratehost.SimulationEngine.utils import (
    convert_currency,
    get_change,
    get_historical,
    get_live,
    get_timeframe,
)


class ExchangeratehostLiveTool(BaseTool):
    """Real-time exchange rates."""

    name: str = "exchangeratehost_live"
    description: str = (
        "Get real-time exchange rates for 168 world currencies. Returns quotes "
        "as currency-pair keys (e.g. USDGBP) mapped to numeric rates. "
        "Optionally specify source (base currency) and currencies to filter."
    )
    args_schema: type[BaseModel] = ExchangeratehostLiveInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_live(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ExchangeratehostHistoricalTool(BaseTool):
    """Historical exchange rates for a specific date."""

    name: str = "exchangeratehost_historical"
    description: str = (
        "Get historical exchange rates for a specific date (YYYY-MM-DD). "
        "Optionally specify source (base currency) and currencies to filter."
    )
    args_schema: type[BaseModel] = ExchangeratehostHistoricalInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_historical(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ExchangeratehostConvertTool(BaseTool):
    """Currency conversion."""

    name: str = "exchangeratehost_convert"
    description: str = (
        "Convert an amount from one currency to another. Specify from_, to, and amount. "
        "Optionally provide a date for historical conversion rates."
    )
    args_schema: type[BaseModel] = ExchangeratehostConvertInput

    def _run(self, **kwargs: Any) -> str:
        try:
            from_ = kwargs.pop("from_")
            return convert_currency(from_=from_, **kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ExchangeratehostTimeframeTool(BaseTool):
    """Time-series exchange rates for a date range."""

    name: str = "exchangeratehost_timeframe"
    description: str = (
        "Get exchange rates for a date range (max 365 days). "
        "Returns daily rates keyed by ISO date. Specify start_date and end_date (YYYY-MM-DD). "
        "Optionally filter by source and currencies."
    )
    args_schema: type[BaseModel] = ExchangeratehostTimeframeInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_timeframe(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ExchangeratehostChangeTool(BaseTool):
    """Currency change/fluctuation between two dates."""

    name: str = "exchangeratehost_change"
    description: str = (
        "Get currency change and fluctuation data between two dates. "
        "Returns start_rate, end_rate, absolute change, and percentage change. "
        "Specify start_date and end_date (YYYY-MM-DD). Optionally filter by source and currencies."
    )
    args_schema: type[BaseModel] = ExchangeratehostChangeInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_change(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ExchangeratehostToolkit:
    """Convenience bundle that exposes all ExchangeRate.host tools."""

    def get_tools(self) -> list[BaseTool]:
        return [
            ExchangeratehostLiveTool(),
            ExchangeratehostHistoricalTool(),
            ExchangeratehostConvertTool(),
            ExchangeratehostTimeframeTool(),
            ExchangeratehostChangeTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    ExchangeratehostLiveTool(),
    ExchangeratehostHistoricalTool(),
    ExchangeratehostConvertTool(),
    ExchangeratehostTimeframeTool(),
    ExchangeratehostChangeTool(),
]
