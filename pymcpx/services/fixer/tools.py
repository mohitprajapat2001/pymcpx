"""
LangChain BaseTool subclasses for the Fixer service.
"""

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from pymcpx.services.fixer.SimulationEngine.models import (
    FixerConvertInput,
    FixerFluctuationInput,
    FixerHistoricalRatesInput,
    FixerLatestRatesInput,
    FixerSymbolsInput,
    FixerTimeSeriesInput,
)
from pymcpx.services.fixer.SimulationEngine.utils import (
    convert_currency,
    get_fluctuation,
    get_historical_rates,
    get_latest_rates,
    get_symbols,
    get_time_series,
)


class FixerSymbolsTool(BaseTool):
    """List all supported currency symbols."""

    name: str = "fixer_symbols"
    description: str = (
        "List all 170+ supported world currencies with their three-letter ISO codes and full names."
    )
    args_schema: type[BaseModel] = FixerSymbolsInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_symbols()
        except Exception as exc:
            return f"Error: {exc}"


class FixerLatestRatesTool(BaseTool):
    """Retrieve latest exchange rates."""

    name: str = "fixer_latest_rates"
    description: str = (
        "Retrieve the latest real-time exchange rate data for 170+ world "
        "currencies. Optionally set a base currency and filter specific symbols."
    )
    args_schema: type[BaseModel] = FixerLatestRatesInput

    def _run(
        self,
        base: str = "EUR",
        symbols: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_latest_rates(base=base, symbols=symbols)
        except Exception as exc:
            return f"Error: {exc}"


class FixerHistoricalRatesTool(BaseTool):
    """Retrieve historical exchange rates for a given date."""

    name: str = "fixer_historical_rates"
    description: str = (
        "Retrieve historical exchange rates for any date back to 1999. "
        "Optionally set a base currency and filter specific symbols."
    )
    args_schema: type[BaseModel] = FixerHistoricalRatesInput

    def _run(
        self,
        date: str,
        base: str = "EUR",
        symbols: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_historical_rates(date=date, base=base, symbols=symbols)
        except Exception as exc:
            return f"Error: {exc}"


class FixerConvertTool(BaseTool):
    """Convert an amount from one currency to another."""

    name: str = "fixer_convert"
    description: str = (
        "Convert any amount from one currency to another using the latest "
        "or historical exchange rates. Supports optional date for historical conversion."
    )
    args_schema: type[BaseModel] = FixerConvertInput

    def _run(
        self,
        from_: str,
        to: str,
        amount: float,
        date: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return convert_currency(from_=from_, to=to, amount=amount, date=date)
        except Exception as exc:
            return f"Error: {exc}"


class FixerTimeSeriesTool(BaseTool):
    """Retrieve daily exchange rates for a date range."""

    name: str = "fixer_timeseries"
    description: str = (
        "Retrieve daily historical exchange rates between two dates "
        "(max 365 day window) for one or multiple currencies."
    )
    args_schema: type[BaseModel] = FixerTimeSeriesInput

    def _run(
        self,
        start_date: str,
        end_date: str,
        base: str = "EUR",
        symbols: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_time_series(
                start_date=start_date,
                end_date=end_date,
                base=base,
                symbols=symbols,
            )
        except Exception as exc:
            return f"Error: {exc}"


class FixerFluctuationTool(BaseTool):
    """Retrieve currency fluctuation data."""

    name: str = "fixer_fluctuation"
    description: str = (
        "Retrieve how currencies fluctuate day-to-day between two dates. "
        "Returns start_rate, end_rate, absolute change, and percentage change."
    )
    args_schema: type[BaseModel] = FixerFluctuationInput

    def _run(
        self,
        start_date: str,
        end_date: str,
        base: str = "EUR",
        symbols: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_fluctuation(
                start_date=start_date,
                end_date=end_date,
                base=base,
                symbols=symbols,
            )
        except Exception as exc:
            return f"Error: {exc}"


class FixerToolkit:
    """Convenience bundle that exposes all fixer tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every fixer tool instance."""
        return [
            FixerSymbolsTool(),
            FixerLatestRatesTool(),
            FixerHistoricalRatesTool(),
            FixerConvertTool(),
            FixerTimeSeriesTool(),
            FixerFluctuationTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    FixerSymbolsTool(),
    FixerLatestRatesTool(),
    FixerHistoricalRatesTool(),
    FixerConvertTool(),
    FixerTimeSeriesTool(),
    FixerFluctuationTool(),
]
