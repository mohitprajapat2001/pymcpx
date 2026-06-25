"""
LangChain BaseTool subclasses for the Marketstack service.
"""

from __future__ import annotations

from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from pymcpx.services.marketstack.SimulationEngine.models import (
    MarketstackBondsInput,
    MarketstackCommoditiesInput,
    MarketstackCompanyRatingsInput,
    MarketstackCurrenciesInput,
    MarketstackDividendsInput,
    MarketstackEdgarCikInput,
    MarketstackEdgarFactsInput,
    MarketstackEdgarSubmissionsInput,
    MarketstackEodInput,
    MarketstackEtfsInput,
    MarketstackExchangesInput,
    MarketstackIndexListInput,
    MarketstackIntradayInput,
    MarketstackListTickersInput,
    MarketstackRealtimePriceInput,
    MarketstackSplitsInput,
    MarketstackTickerInfoInput,
    MarketstackTimezonesInput,
)
from pymcpx.services.marketstack.SimulationEngine.utils import (
    get_bonds,
    get_commodity_price,
    get_company_ratings,
    get_currencies,
    get_dividends,
    get_edgar_cik,
    get_edgar_facts,
    get_edgar_submissions,
    get_eod_data,
    get_etfs,
    get_exchanges,
    get_indices,
    get_intraday_data,
    get_realtime_price,
    get_splits,
    get_ticker_info,
    get_timezones,
    list_tickers,
)


class MarketstackEodTool(BaseTool):
    """Retrieve End-of-Day (EOD) data for stock symbols."""

    name: str = "marketstack_eod"
    description: str = (
        "Retrieve End-of-Day (EOD) data for one or multiple stock tickers. "
        "Supports filtering by date, latest date, exchange, sorting, and pagination."
    )
    args_schema: type[BaseModel] = MarketstackEodInput

    def _run(
        self,
        symbols: str,
        date: str | None = None,
        latest: bool = False,
        exchange: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_eod_data(
                symbols=symbols,
                date=date,
                latest=latest,
                exchange=exchange,
                date_from=date_from,
                date_to=date_to,
                sort=sort,
                limit=limit,
                offset=offset,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackIntradayTool(BaseTool):
    """Retrieve Intraday stock prices."""

    name: str = "marketstack_intraday"
    description: str = (
        "Retrieve intraday stock prices at intervals from 1min to 1hour. "
        "Supports filters for specific dates, latest data, exchange, sort "
        "order, and after-hours trading."
    )
    args_schema: type[BaseModel] = MarketstackIntradayInput

    def _run(
        self,
        symbols: str,
        interval: str | None = None,
        date: str | None = None,
        latest: bool = False,
        exchange: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        after_hours: bool | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_intraday_data(
                symbols=symbols,
                interval=interval,
                date=date,
                latest=latest,
                exchange=exchange,
                date_from=date_from,
                date_to=date_to,
                sort=sort,
                limit=limit,
                offset=offset,
                after_hours=after_hours,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackRealtimePriceTool(BaseTool):
    """Retrieve Real-time Stock Market Price."""

    name: str = "marketstack_realtime_price"
    description: str = (
        "Retrieve real-time stock price data for a single symbol "
        "(e.g. 'AAPL') from supported exchanges."
    )
    args_schema: type[BaseModel] = MarketstackRealtimePriceInput

    def _run(self, ticker: str, exchange: str | None = None, **kwargs: Any) -> str:
        try:
            return get_realtime_price(ticker=ticker, exchange=exchange)
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackCommoditiesTool(BaseTool):
    """Retrieve Commodity prices (real-time or historical)."""

    name: str = "marketstack_commodities"
    description: str = (
        "Retrieve real-time or historical commodity prices for 70+ world "
        "commodities (e.g. 'aluminum', 'gold') with daily, weekly, monthly "
        "frequency filters."
    )
    args_schema: type[BaseModel] = MarketstackCommoditiesInput

    def _run(
        self,
        commodity_name: str,
        date_from: str | None = None,
        date_to: str | None = None,
        frequency: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_commodity_price(
                commodity_name=commodity_name,
                date_from=date_from,
                date_to=date_to,
                frequency=frequency,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackCompanyRatingsTool(BaseTool):
    """Retrieve analyst ratings and price targets."""

    name: str = "marketstack_company_ratings"
    description: str = (
        "Retrieve buy/sell/hold analyst ratings and price targets "
        "for a list of ticker symbols, including historical target trends."
    )
    args_schema: type[BaseModel] = MarketstackCompanyRatingsInput

    def _run(
        self,
        ticker: str,
        date_from: str | None = None,
        date_to: str | None = None,
        rated: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_company_ratings(
                ticker=ticker,
                date_from=date_from,
                date_to=date_to,
                rated=rated,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackSplitsTool(BaseTool):
    """Retrieve stock split history."""

    name: str = "marketstack_splits"
    description: str = (
        "Retrieve stock split factors and split history for specified tickers or a single symbol."
    )
    args_schema: type[BaseModel] = MarketstackSplitsInput

    def _run(
        self,
        symbols: str | None = None,
        symbol: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_splits(
                symbols=symbols,
                symbol=symbol,
                date_from=date_from,
                date_to=date_to,
                sort=sort,
                limit=limit,
                offset=offset,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackDividendsTool(BaseTool):
    """Retrieve stock dividend history."""

    name: str = "marketstack_dividends"
    description: str = (
        "Retrieve dividend payments, ex-dividend dates, and "
        "distribution details for specified tickers or a single symbol."
    )
    args_schema: type[BaseModel] = MarketstackDividendsInput

    def _run(
        self,
        symbols: str | None = None,
        symbol: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_dividends(
                symbols=symbols,
                symbol=symbol,
                date_from=date_from,
                date_to=date_to,
                sort=sort,
                limit=limit,
                offset=offset,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackTickerInfoTool(BaseTool):
    """Retrieve detailed ticker properties."""

    name: str = "marketstack_ticker_info"
    description: str = (
        "Retrieve detailed ticker properties such as sector, industry, "
        "employees, founding date, address, and listing exchanges."
    )
    args_schema: type[BaseModel] = MarketstackTickerInfoInput

    def _run(
        self,
        symbol: str,
        exchange: str | None = None,
        use_tickerinfo_endpoint: bool = False,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_ticker_info(
                symbol=symbol,
                exchange=exchange,
                use_tickerinfo_endpoint=use_tickerinfo_endpoint,
                limit=limit,
                offset=offset,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackListTickersTool(BaseTool):
    """Search and list stock tickers."""

    name: str = "marketstack_list_tickers"
    description: str = (
        "Search and list tickers, filtrable by a search query or a specific stock exchange."
    )
    args_schema: type[BaseModel] = MarketstackListTickersInput

    def _run(
        self,
        search: str | None = None,
        exchange: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return list_tickers(
                search=search,
                exchange=exchange,
                limit=limit,
                offset=offset,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackIndexListTool(BaseTool):
    """List indices or get info for a specific index."""

    name: str = "marketstack_indices"
    description: str = (
        "Retrieve listings of supported stock market indices or "
        "detailed quotes and performance metrics for a specific index."
    )
    args_schema: type[BaseModel] = MarketstackIndexListInput

    def _run(
        self,
        index: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_indices(
                index=index,
                limit=limit,
                offset=offset,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackExchangesTool(BaseTool):
    """Query stock exchanges details, listed tickers, EOD, or Intraday data."""

    name: str = "marketstack_exchanges"
    description: str = (
        "List supported exchanges, search exchanges, or query specific exchange "
        "sub-endpoints (listed tickers, EOD, EOD latest, EOD specific date, "
        "Intraday, Intraday latest, Intraday specific date) using MIC identification."
    )
    args_schema: type[BaseModel] = MarketstackExchangesInput

    def _run(
        self,
        mic: str | None = None,
        endpoint_type: str = "info",
        symbols: str | None = None,
        date: str | None = None,
        interval: str | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        sort: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        search: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_exchanges(
                mic=mic,
                endpoint_type=endpoint_type,
                symbols=symbols,
                date=date,
                interval=interval,
                date_from=date_from,
                date_to=date_to,
                sort=sort,
                limit=limit,
                offset=offset,
                search=search,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackCurrenciesTool(BaseTool):
    """List supported currencies."""

    name: str = "marketstack_currencies"
    description: str = "List supported currencies (default 10 per page)."
    args_schema: type[BaseModel] = MarketstackCurrenciesInput

    def _run(
        self,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_currencies(limit=limit, offset=offset)
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackTimezonesTool(BaseTool):
    """List supported timezones."""

    name: str = "marketstack_timezones"
    description: str = "List supported timezones (default 10 per page)."
    args_schema: type[BaseModel] = MarketstackTimezonesInput

    def _run(
        self,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_timezones(limit=limit, offset=offset)
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackBondsTool(BaseTool):
    """Retrieve government bond data."""

    name: str = "marketstack_bonds"
    description: str = (
        "Retrieve real-time government bond yield data for leading "
        "countries or list supported countries."
    )
    args_schema: type[BaseModel] = MarketstackBondsInput

    def _run(
        self,
        country: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_bonds(country=country, limit=limit, offset=offset)
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackEtfsTool(BaseTool):
    """Retrieve ETF listings or holdings."""

    name: str = "marketstack_etfs"
    description: str = (
        "List all supported ETF symbols or retrieve detailed "
        "holdings and portfolio weights for a specific ETF."
    )
    args_schema: type[BaseModel] = MarketstackEtfsInput

    def _run(
        self,
        ticker: str | None = None,
        list_type: str = "ticker",
        date_from: str | None = None,
        date_to: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_etfs(
                ticker=ticker,
                list_type=list_type,
                date_from=date_from,
                date_to=date_to,
                limit=limit,
                offset=offset,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackEdgarCikTool(BaseTool):
    """Search CIK code by company name, or find company name by CIK."""

    name: str = "marketstack_edgar_cik"
    description: str = (
        "Search for CIK (Central Index Key) codes by company name, "
        "or look up company names/addresses for a specific CIK."
    )
    args_schema: type[BaseModel] = MarketstackEdgarCikInput

    def _run(
        self,
        company_name: str | None = None,
        cik_code: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_edgar_cik(
                company_name=company_name,
                cik_code=cik_code,
                limit=limit,
                offset=offset,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackEdgarSubmissionsTool(BaseTool):
    """Query SEC EDGAR submission histories."""

    name: str = "marketstack_edgar_submissions"
    description: str = (
        "Query SEC EDGAR submission histories and filing metadata for a specific CIK code."
    )
    args_schema: type[BaseModel] = MarketstackEdgarSubmissionsInput

    def _run(
        self,
        cik_code: str | None = None,
        cik_code_name: str | None = None,
        report_from: str | None = None,
        report_to: str | None = None,
        filing_from: str | None = None,
        filing_to: str | None = None,
        accession_number: str | None = None,
        **kwargs: Any,
    ) -> str:
        try:
            return get_edgar_submissions(
                cik_code=cik_code,
                cik_code_name=cik_code_name,
                report_from=report_from,
                report_to=report_to,
                filing_from=filing_from,
                filing_to=filing_to,
                accession_number=accession_number,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackEdgarFactsTool(BaseTool):
    """Query company facts, concepts, or US GAAP Accounts Payable."""

    name: str = "marketstack_edgar_facts"
    description: str = (
        "Query company facts, concept taxonomies, US GAAP Accounts Payable, "
        "or Accounts Payable frame values in a specific unit."
    )
    args_schema: type[BaseModel] = MarketstackEdgarFactsInput

    def _run(
        self,
        cik_code: str,
        query_type: str = "facts",
        frame: str | None = None,
        unit: str | None = "USD",
        **kwargs: Any,
    ) -> str:
        try:
            return get_edgar_facts(
                cik_code=cik_code,
                query_type=query_type,
                frame=frame,
                unit=unit,
            )
        except Exception as exc:
            return f"Error: {exc}"


class MarketstackToolkit:
    """Convenience bundle that exposes all marketstack tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every marketstack tool instance."""
        return [
            MarketstackEodTool(),
            MarketstackIntradayTool(),
            MarketstackRealtimePriceTool(),
            MarketstackCommoditiesTool(),
            MarketstackCompanyRatingsTool(),
            MarketstackSplitsTool(),
            MarketstackDividendsTool(),
            MarketstackTickerInfoTool(),
            MarketstackListTickersTool(),
            MarketstackIndexListTool(),
            MarketstackExchangesTool(),
            MarketstackCurrenciesTool(),
            MarketstackTimezonesTool(),
            MarketstackBondsTool(),
            MarketstackEtfsTool(),
            MarketstackEdgarCikTool(),
            MarketstackEdgarSubmissionsTool(),
            MarketstackEdgarFactsTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    MarketstackEodTool(),
    MarketstackIntradayTool(),
    MarketstackRealtimePriceTool(),
    MarketstackCommoditiesTool(),
    MarketstackCompanyRatingsTool(),
    MarketstackSplitsTool(),
    MarketstackDividendsTool(),
    MarketstackTickerInfoTool(),
    MarketstackListTickersTool(),
    MarketstackIndexListTool(),
    MarketstackExchangesTool(),
    MarketstackCurrenciesTool(),
    MarketstackTimezonesTool(),
    MarketstackBondsTool(),
    MarketstackEtfsTool(),
    MarketstackEdgarCikTool(),
    MarketstackEdgarSubmissionsTool(),
    MarketstackEdgarFactsTool(),
]
