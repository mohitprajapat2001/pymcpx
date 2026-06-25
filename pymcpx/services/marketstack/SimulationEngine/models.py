"""
Pydantic input models for the Marketstack service tools.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class MarketstackEodInput(BaseModel):
    """Input schema for End-of-Day (EOD) stock data lookup."""

    symbols: str = Field(
        description="One or more comma-separated ticker symbols (e.g., 'AAPL,MSFT')."
    )
    date: str | None = Field(
        default=None,
        description="Filter results for a specific date (Format 'YYYY-MM-DD').",
    )
    latest: bool = Field(
        default=False,
        description="If True, retrieves the most recent EOD data point for the requested symbols.",
    )
    exchange: str | None = Field(
        default=None,
        description="Filter results based on a specific stock exchange MIC (e.g., 'XNAS').",
    )
    date_from: str | None = Field(
        default=None,
        description="Filter results from this date inclusive (Format 'YYYY-MM-DD').",
    )
    date_to: str | None = Field(
        default=None,
        description="Filter results up to this date inclusive (Format 'YYYY-MM-DD').",
    )
    sort: str | None = Field(
        default=None,
        description="Sort order: 'ASC' for oldest first, 'DESC' for newest first.",
    )
    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10, max 1000).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset (number of results to skip).",
    )


class MarketstackIntradayInput(BaseModel):
    """Input schema for Intraday stock data lookup."""

    symbols: str = Field(
        description=(
            "One or more comma-separated ticker symbols. "
            "Note: replace dots with hyphens (e.g., 'BRK.B' -> 'BRK-B')."
        )
    )
    interval: str | None = Field(
        default=None,
        description=(
            "Intraday aggregation interval. E.g. '1min', '5min', "
            "'10min', '15min', '30min', '1hour'."
        ),
    )
    date: str | None = Field(
        default=None,
        description="Filter results for a specific date or time (Format 'YYYY-MM-DD' or ISO-8601).",
    )
    latest: bool = Field(
        default=False,
        description="If True, retrieves the most recent intraday bar for the requested symbols.",
    )
    exchange: str | None = Field(
        default=None,
        description="Filter results based on a specific stock exchange MIC (e.g., 'XNAS').",
    )
    date_from: str | None = Field(
        default=None,
        description="Filter results from this date inclusive (Format 'YYYY-MM-DD').",
    )
    date_to: str | None = Field(
        default=None,
        description="Filter results up to this date inclusive (Format 'YYYY-MM-DD').",
    )
    sort: str | None = Field(
        default=None,
        description="Sort order: 'ASC' or 'DESC'.",
    )
    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10, max 1000).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset (number of results to skip).",
    )
    after_hours: bool | None = Field(
        default=None,
        description="If True, includes pre and post market data if available.",
    )


class MarketstackRealtimePriceInput(BaseModel):
    """Input schema for Real-time Stock Market Price lookup."""

    ticker: str = Field(
        description="Ticker symbol for which to retrieve the real-time stock price (e.g., 'AAPL')."
    )
    exchange: str | None = Field(
        default=None,
        description="Optional exchange MIC filter (e.g., 'NASDAQ').",
    )


class MarketstackCommoditiesInput(BaseModel):
    """Input schema for commodity price lookup (real-time or historical)."""

    commodity_name: str = Field(
        description="Specify the commodity name for which to receive the price (e.g., 'aluminum')."
    )
    date_from: str | None = Field(
        default=None,
        description="Filter historical results from this date inclusive (Format 'YYYY-MM-DD').",
    )
    date_to: str | None = Field(
        default=None,
        description="Filter historical results up to this date inclusive (Format 'YYYY-MM-DD').",
    )
    frequency: str | None = Field(
        default=None,
        description=(
            "Specify the frequency of the historical prices: "
            "'daily', 'weekly', 'monthly', 'quarterly', 'yearly'."
        ),
    )


class MarketstackCompanyRatingsInput(BaseModel):
    """Input schema for analyst ratings lookup."""

    ticker: str = Field(
        description="One or more comma-separated ticker symbols (e.g., 'AAPL,MSFT')."
    )
    date_from: str | None = Field(
        default=None,
        description="Filter results from this date inclusive (Format 'YYYY-MM-DD').",
    )
    date_to: str | None = Field(
        default=None,
        description="Filter results up to this date inclusive (Format 'YYYY-MM-DD').",
    )
    rated: str | None = Field(
        default=None,
        description="Filter response on rating type: 'buy', 'sell', or 'hold'.",
    )


class MarketstackSplitsInput(BaseModel):
    """Input schema for stock split history lookup."""

    symbols: str | None = Field(
        default=None,
        description=(
            "One or more comma-separated ticker symbols (e.g., 'AAPL,MSFT'). "
            "Use this or single 'symbol'."
        ),
    )
    symbol: str | None = Field(
        default=None,
        description="If querying splits history for a single ticker via /tickers/{symbol}/splits.",
    )
    date_from: str | None = Field(
        default=None,
        description="Filter results from this date inclusive (Format 'YYYY-MM-DD').",
    )
    date_to: str | None = Field(
        default=None,
        description="Filter results up to this date inclusive (Format 'YYYY-MM-DD').",
    )
    sort: str | None = Field(
        default=None,
        description="Sort order: 'ASC' or 'DESC'.",
    )
    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10, max 1000).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset (number of results to skip).",
    )


class MarketstackDividendsInput(BaseModel):
    """Input schema for stock dividend history lookup."""

    symbols: str | None = Field(
        default=None,
        description=(
            "One or more comma-separated ticker symbols (e.g., 'AAPL,MSFT'). "
            "Use this or single 'symbol'."
        ),
    )
    symbol: str | None = Field(
        default=None,
        description=(
            "If querying dividends history for a single ticker " "via /tickers/{symbol}/dividends."
        ),
    )
    date_from: str | None = Field(
        default=None,
        description="Filter results from this date inclusive (Format 'YYYY-MM-DD').",
    )
    date_to: str | None = Field(
        default=None,
        description="Filter results up to this date inclusive (Format 'YYYY-MM-DD').",
    )
    sort: str | None = Field(
        default=None,
        description="Sort order: 'ASC' or 'DESC'.",
    )
    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10, max 1000).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset (number of results to skip).",
    )


class MarketstackTickerInfoInput(BaseModel):
    """Input schema for ticker information lookup."""

    symbol: str = Field(
        description=(
            "The ticker symbol to look up (e.g., 'AAPL'). For multiple symbols, "
            "separate by commas if using 'use_tickerinfo_endpoint'."
        )
    )
    exchange: str | None = Field(
        default=None,
        description="Filter results based on specific stock exchange MIC.",
    )
    use_tickerinfo_endpoint: bool = Field(
        default=False,
        description="If True, queries the bulk /tickerinfo endpoint instead of /tickers/{symbol}.",
    )
    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset.",
    )


class MarketstackListTickersInput(BaseModel):
    """Input schema for searching/listing stock tickers."""

    search: str | None = Field(
        default=None,
        description="Search term to filter tickers by name or symbol (e.g., 'Apple').",
    )
    exchange: str | None = Field(
        default=None,
        description="Filter results by a specific stock exchange MIC.",
    )
    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset.",
    )


class MarketstackIndexListInput(BaseModel):
    """Input schema for stock market index listings and details."""

    index: str | None = Field(
        default=None,
        description=(
            "Benchmark/index identifier to fetch specific details "
            "(e.g., 'australia_all_ordinaries'). If empty, lists indices."
        ),
    )
    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10, for index listing).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset (for index listing).",
    )


class MarketstackExchangesInput(BaseModel):
    """Input schema for querying stock exchanges."""

    mic: str | None = Field(
        default=None,
        description=(
            "Optional stock exchange MIC identifier (e.g., 'XNAS'). "
            "If omitted, list all exchanges."
        ),
    )
    endpoint_type: str = Field(
        default="info",
        description=(
            "Sub-endpoint type. One of: 'info' (general exchange details), "
            "'tickers' (tickers listed on exchange), 'eod' (EOD data for symbols on exchange), "
            "'eod_latest', 'eod_date', 'intraday' (intraday data for exchange symbols), "
            "'intraday_latest', 'intraday_date'."
        ),
    )
    symbols: str | None = Field(
        default=None,
        description=(
            "Comma-separated ticker symbols. Required for " "'eod' and 'intraday' sub-endpoints."
        ),
    )
    date: str | None = Field(
        default=None,
        description="Specific date for date-based sub-endpoints (Format 'YYYY-MM-DD' or ISO-8601).",
    )
    interval: str | None = Field(
        default=None,
        description="Intraday aggregation interval (e.g., '1min').",
    )
    date_from: str | None = Field(
        default=None,
        description="Filter results from this date inclusive (Format 'YYYY-MM-DD').",
    )
    date_to: str | None = Field(
        default=None,
        description="Filter results up to this date inclusive (Format 'YYYY-MM-DD').",
    )
    sort: str | None = Field(
        default=None,
        description="Sort order: 'ASC' or 'DESC'.",
    )
    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset.",
    )
    search: str | None = Field(
        default=None,
        description=(
            "Search term to filter exchanges by name or country (only when MIC is omitted)."
        ),
    )


class MarketstackCurrenciesInput(BaseModel):
    """Input schema for listing supported currencies."""

    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset.",
    )


class MarketstackTimezonesInput(BaseModel):
    """Input schema for listing supported timezones."""

    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset.",
    )


class MarketstackBondsInput(BaseModel):
    """Input schema for government bonds data."""

    country: str | None = Field(
        default=None,
        description=(
            "Specify country name to receive real-time government bond data "
            "(e.g., 'united states'). If omitted, lists supported countries."
        ),
    )
    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10, only when listing countries).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset (only when listing countries).",
    )


class MarketstackEtfsInput(BaseModel):
    """Input schema for ETF holdings information."""

    ticker: str | None = Field(
        default=None,
        description=(
            "ETF ticker symbol (e.g., 'IVV') to retrieve holdings info. "
            "If omitted, lists supported ETF tickers."
        ),
    )
    list_type: str = Field(
        default="ticker",
        description="ETF listing type, currently only 'ticker' is supported.",
    )
    date_from: str | None = Field(
        default=None,
        description="Filter holdings from this date inclusive (Format 'YYYY-MM-DD').",
    )
    date_to: str | None = Field(
        default=None,
        description="Filter holdings up to this date inclusive (Format 'YYYY-MM-DD').",
    )
    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset.",
    )


class MarketstackEdgarCikInput(BaseModel):
    """Input schema for CIK lookup by company name or vice versa."""

    company_name: str | None = Field(
        default=None,
        description="Company name or partial name (min 3 letters) to search for CIK codes.",
    )
    cik_code: str | None = Field(
        default=None,
        description="10-digit Central Index Key (with leading zeros) to find company details.",
    )
    limit: int | None = Field(
        default=None,
        description="Pagination limit (default 10, when searching by company name).",
    )
    offset: int | None = Field(
        default=None,
        description="Pagination offset (when searching by company name).",
    )


class MarketstackEdgarSubmissionsInput(BaseModel):
    """Input schema for SEC submissions query."""

    cik_code: str | None = Field(
        default=None,
        description="10-digit Central Index Key (with leading zeros) of the company.",
    )
    cik_code_name: str | None = Field(
        default=None,
        description=(
            "10-digit CIK code name ending with '-submissions.json' "
            "(e.g., 'CIK0001509697-submissions.json')."
        ),
    )
    report_from: str | None = Field(
        default=None,
        description="Filter filings by report date from this date inclusive (Format 'YYYY-MM-DD').",
    )
    report_to: str | None = Field(
        default=None,
        description="Filter filings by report date to this date inclusive (Format 'YYYY-MM-DD').",
    )
    filing_from: str | None = Field(
        default=None,
        description="Filter filings by filing date from this date inclusive (Format 'YYYY-MM-DD').",
    )
    filing_to: str | None = Field(
        default=None,
        description="Filter filings by filing date to this date inclusive (Format 'YYYY-MM-DD').",
    )
    accession_number: str | None = Field(
        default=None,
        description="Filter filings by exact SEC accession number.",
    )


class MarketstackEdgarFactsInput(BaseModel):
    """Input schema for company facts and concepts (e.g., Accounts Payable)."""

    cik_code: str = Field(
        description="10-digit Central Index Key (with leading zeros) of the company."
    )
    query_type: str = Field(
        default="facts",
        description=(
            "Type of facts query: 'facts' (all company concepts), "
            "'accounts_payable' (US GAAP Accounts Payable), "
            "'accounts_payable_frames' (US GAAP Accounts Payable in a calendar period and unit)."
        ),
    )
    frame: str | None = Field(
        default=None,
        description=(
            "Calendar period code (e.g., 'CY2023Q1I'). Required for 'accounts_payable_frames'."
        ),
    )
    unit: str | None = Field(
        default="USD",
        description=(
            "Unit of measure. Typically 'USD' or 'USD-per-shares'. "
            "Defaults to 'USD'. Only used in 'accounts_payable_frames'."
        ),
    )
