"""
HTTP client for the Marketstack API.
"""

from __future__ import annotations

import json
import os
from typing import Any

import httpx

BASE_URL = "https://api.marketstack.com/v2"


def _get_access_key() -> str:
    """Retrieve the Marketstack API access key from the environment."""
    key = os.environ.get("MARKETSTACK_ACCESS_KEY")
    if not key:
        raise ValueError(
            "MARKETSTACK_ACCESS_KEY environment variable is not set. "
            "Please set it to your Marketstack API access key."
        )
    return key


def _build_params(access_key: str, **kwargs: Any) -> dict[str, Any]:
    """Build query parameters dict, dropping None values and encoding booleans."""
    params: dict[str, Any] = {"access_key": access_key}
    for k, v in kwargs.items():
        if v is not None:
            if isinstance(v, bool):
                params[k] = "true" if v else "false"
            else:
                params[k] = v
    return params


def _format_response(response_text: str) -> str:
    """Pretty-print a JSON response, or return raw text if it's not JSON."""
    try:
        data = json.loads(response_text)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, ValueError):
        return response_text


def get_eod_data(
    symbols: str,
    date: str | None = None,
    latest: bool = False,
    exchange: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    sort: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> str:
    """Retrieve End-of-Day (EOD) data for one or multiple stock tickers."""
    access_key = _get_access_key()
    limit = limit or 10

    if latest:
        url = f"{BASE_URL}/eod/latest"
        params = _build_params(
            access_key, symbols=symbols, exchange=exchange, sort=sort, limit=limit, offset=offset
        )
    elif date:
        url = f"{BASE_URL}/eod/{date}"
        params = _build_params(
            access_key, symbols=symbols, exchange=exchange, sort=sort, limit=limit, offset=offset
        )
    else:
        url = f"{BASE_URL}/eod"
        params = _build_params(
            access_key,
            symbols=symbols,
            exchange=exchange,
            date_from=date_from,
            date_to=date_to,
            sort=sort,
            limit=limit,
            offset=offset,
        )

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_intraday_data(
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
) -> str:
    """Retrieve Intraday data for one or multiple stock tickers."""
    access_key = _get_access_key()
    limit = limit or 10

    if latest:
        url = f"{BASE_URL}/intraday/latest"
        params = _build_params(
            access_key,
            symbols=symbols,
            interval=interval,
            exchange=exchange,
            after_hours=after_hours,
        )
    elif date:
        url = f"{BASE_URL}/intraday/{date}"
        params = _build_params(
            access_key,
            symbols=symbols,
            interval=interval,
            exchange=exchange,
            limit=limit,
            offset=offset,
            after_hours=after_hours,
        )
    else:
        url = f"{BASE_URL}/intraday"
        params = _build_params(
            access_key,
            symbols=symbols,
            interval=interval,
            exchange=exchange,
            date_from=date_from,
            date_to=date_to,
            sort=sort,
            limit=limit,
            offset=offset,
            after_hours=after_hours,
        )

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_realtime_price(ticker: str, exchange: str | None = None) -> str:
    """Retrieve Real-time Stock Market Prices."""
    access_key = _get_access_key()
    params = _build_params(access_key, ticker=ticker, exchange=exchange)

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/stockprice", params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_commodity_price(
    commodity_name: str,
    date_from: str | None = None,
    date_to: str | None = None,
    frequency: str | None = None,
) -> str:
    """Retrieve commodity prices (real-time or historical)."""
    access_key = _get_access_key()

    if date_from or date_to or frequency:
        url = f"{BASE_URL}/commoditieshistory"
        params = _build_params(
            access_key,
            commodity_name=commodity_name,
            date_from=date_from,
            date_to=date_to,
            frequency=frequency,
        )
    else:
        url = f"{BASE_URL}/commodities"
        params = _build_params(access_key, commodity_name=commodity_name)

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_company_ratings(
    ticker: str,
    date_from: str | None = None,
    date_to: str | None = None,
    rated: str | None = None,
) -> str:
    """Retrieve analyst ratings for a company."""
    access_key = _get_access_key()
    limit = limit or 10
    params = _build_params(
        access_key, ticker=ticker, date_from=date_from, date_to=date_to, rated=rated
    )

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/companyratings", params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_splits(
    symbols: str | None = None,
    symbol: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    sort: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> str:
    """Retrieve stock splits factor."""
    access_key = _get_access_key()
    limit = limit or 10

    if symbol:
        url = f"{BASE_URL}/tickers/{symbol}/splits"
        params = _build_params(
            access_key,
            exchange=None,
            limit=limit,
            offset=offset,
            date_from=date_from,
            date_to=date_to,
            sort=sort,
        )
    else:
        url = f"{BASE_URL}/splits"
        params = _build_params(
            access_key,
            symbols=symbols,
            date_from=date_from,
            date_to=date_to,
            sort=sort,
            limit=limit,
            offset=offset,
        )

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_dividends(
    symbols: str | None = None,
    symbol: str | None = None,
    date_from: str | None = None,
    date_to: str | None = None,
    sort: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> str:
    """Retrieve dividends data."""
    access_key = _get_access_key()
    limit = limit or 10

    if symbol:
        url = f"{BASE_URL}/tickers/{symbol}/dividends"
        params = _build_params(
            access_key,
            exchange=None,
            limit=limit,
            offset=offset,
            date_from=date_from,
            date_to=date_to,
            sort=sort,
        )
    else:
        url = f"{BASE_URL}/dividends"
        params = _build_params(
            access_key,
            symbols=symbols,
            date_from=date_from,
            date_to=date_to,
            sort=sort,
            limit=limit,
            offset=offset,
        )

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_ticker_info(
    symbol: str,
    exchange: str | None = None,
    use_tickerinfo_endpoint: bool = False,
    limit: int | None = None,
    offset: int | None = None,
) -> str:
    """Retrieve detailed ticker or stock symbol information."""
    access_key = _get_access_key()

    if use_tickerinfo_endpoint:
        url = f"{BASE_URL}/tickerinfo"
        params = _build_params(access_key, ticker=symbol)
    else:
        url = f"{BASE_URL}/tickers/{symbol}"
        params = _build_params(access_key, exchange=exchange, limit=limit, offset=offset)

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def list_tickers(
    search: str | None = None,
    exchange: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> str:
    """Search or list supported stock tickers."""
    access_key = _get_access_key()
    limit = limit or 10
    params = _build_params(access_key, search=search, exchange=exchange, limit=limit, offset=offset)

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/tickerslist", params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_indices(
    index: str | None = None, limit: int | None = None, offset: int | None = None
) -> str:
    """Retrieve stock index listings or details."""
    access_key = _get_access_key()

    if index:
        url = f"{BASE_URL}/indexinfo"
        params = _build_params(access_key, index=index)
    else:
        limit = limit or 10
        url = f"{BASE_URL}/indexlist"
        params = _build_params(access_key, limit=limit, offset=offset)

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_exchanges(
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
) -> str:
    """Retrieve exchanges list, exchange details, listed tickers, EOD, or Intraday data."""
    access_key = _get_access_key()

    if not mic:
        limit = limit or 10
        url = f"{BASE_URL}/exchanges"
        params = _build_params(access_key, limit=limit, offset=offset, search=search)
    else:
        endpoint_type = endpoint_type.lower().strip()
        if endpoint_type == "info":
            url = f"{BASE_URL}/exchanges/{mic}"
            params = _build_params(access_key)
        elif endpoint_type == "tickers":
            url = f"{BASE_URL}/exchanges/{mic}/tickers"
            params = _build_params(access_key, limit=limit, offset=offset)
        elif endpoint_type == "eod":
            url = f"{BASE_URL}/exchanges/{mic}/eod"
            params = _build_params(
                access_key,
                symbols=symbols,
                date_from=date_from,
                date_to=date_to,
                sort=sort,
                limit=limit,
                offset=offset,
            )
        elif endpoint_type == "eod_latest":
            url = f"{BASE_URL}/exchanges/{mic}/eod/latest"
            params = _build_params(access_key, symbols=symbols)
        elif endpoint_type == "eod_date":
            url = f"{BASE_URL}/exchanges/{mic}/eod/{date}"
            params = _build_params(access_key, symbols=symbols, limit=limit, offset=offset)
        elif endpoint_type == "intraday":
            url = f"{BASE_URL}/exchanges/{mic}/intraday"
            params = _build_params(
                access_key,
                symbols=symbols,
                interval=interval,
                date_from=date_from,
                date_to=date_to,
                sort=sort,
                limit=limit,
                offset=offset,
            )
        elif endpoint_type == "intraday_latest":
            url = f"{BASE_URL}/exchanges/{mic}/intraday/latest"
            params = _build_params(access_key, symbols=symbols, interval=interval)
        elif endpoint_type == "intraday_date":
            url = f"{BASE_URL}/exchanges/{mic}/intraday/{date}"
            params = _build_params(
                access_key, symbols=symbols, interval=interval, limit=limit, offset=offset
            )
        else:
            raise ValueError(f"Unknown endpoint_type: {endpoint_type}")

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_currencies(limit: int | None = None, offset: int | None = None) -> str:
    """Retrieve paginated list of supported currencies."""
    access_key = _get_access_key()
    limit = limit or 10
    params = _build_params(access_key, limit=limit, offset=offset)

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/currencies", params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_timezones(limit: int | None = None, offset: int | None = None) -> str:
    """Retrieve paginated list of supported timezones."""
    access_key = _get_access_key()
    limit = limit or 10
    params = _build_params(access_key, limit=limit, offset=offset)

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/timezones", params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_bonds(
    country: str | None = None, limit: int | None = None, offset: int | None = None
) -> str:
    """Retrieve government bonds yield details."""
    access_key = _get_access_key()

    if country:
        url = f"{BASE_URL}/bond"
        params = _build_params(access_key, country=country)
    else:
        limit = limit or 10
        url = f"{BASE_URL}/bondlist"
        params = _build_params(access_key, limit=limit, offset=offset)

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_etfs(
    ticker: str | None = None,
    list_type: str = "ticker",
    date_from: str | None = None,
    date_to: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> str:
    """Retrieve ETF listings or holdings."""
    access_key = _get_access_key()

    if ticker:
        url = f"{BASE_URL}/etfholdings"
        params = _build_params(access_key, ticker=ticker, date_from=date_from, date_to=date_to)
    else:
        limit = limit or 10
        url = f"{BASE_URL}/etflist"
        params = _build_params(access_key, list=list_type, limit=limit, offset=offset)

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_edgar_cik(
    company_name: str | None = None,
    cik_code: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> str:
    """Retrieve CIK from company name or vice versa."""
    access_key = _get_access_key()

    if company_name:
        limit = limit or 10
        url = f"{BASE_URL}/cik_code"
        params = _build_params(access_key, company_name=company_name, limit=limit, offset=offset)
    elif cik_code:
        url = f"{BASE_URL}/company_name"
        params = _build_params(access_key, cik_code=cik_code)
    else:
        raise ValueError("Must specify either company_name or cik_code")

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_edgar_submissions(
    cik_code: str | None = None,
    cik_code_name: str | None = None,
    report_from: str | None = None,
    report_to: str | None = None,
    filing_from: str | None = None,
    filing_to: str | None = None,
    accession_number: str | None = None,
) -> str:
    """Retrieve submissions details from CIK."""
    access_key = _get_access_key()

    if not cik_code and not cik_code_name:
        raise ValueError("Must specify at least one of cik_code or cik_code_name")

    params = _build_params(
        access_key,
        cik_code=cik_code,
        cik_code_name=cik_code_name,
        report_from=report_from,
        report_to=report_to,
        filing_from=filing_from,
        filing_to=filing_to,
        accession_number=accession_number,
    )

    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/submissions", params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_edgar_facts(
    cik_code: str,
    query_type: str = "facts",
    frame: str | None = None,
    unit: str | None = "USD",
) -> str:
    """Retrieve facts, concepts, or Accounts Payable frame details."""
    access_key = _get_access_key()
    query_type = query_type.lower().strip()

    if query_type == "facts":
        url = f"{BASE_URL}/company_facts"
        params = _build_params(access_key, cik_code=cik_code)
    elif query_type == "accounts_payable":
        url = f"{BASE_URL}/concept/accounts_payable"
        params = _build_params(access_key, cik_code=cik_code)
    elif query_type == "accounts_payable_frames":
        if not frame:
            raise ValueError("frame parameter is required for query_type='accounts_payable_frames'")
        # unit goes into path
        url = f"{BASE_URL}/frames/accounts_payable/{unit}"
        params = _build_params(access_key, frame=frame)
    else:
        raise ValueError(f"Unknown query_type: {query_type}")

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Marketstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)
