from __future__ import annotations

import json
import os
from typing import Any

import httpx

BASE_URL = "https://api.exchangerate.host"


def _get_access_key() -> str:
    key = os.environ.get("EXCHANGERATEHOST_ACCESS_KEY")
    if not key:
        raise ValueError(
            "EXCHANGERATEHOST_ACCESS_KEY environment variable is not set. "
            "Please set it to your ExchangeRate.host API access key."
        )
    return key


def _build_params(access_key: str, **kwargs: Any) -> dict[str, Any]:
    params: dict[str, Any] = {"access_key": access_key}
    for k, v in kwargs.items():
        if v is not None:
            params[k] = v
    return params


def _format_response(response_text: str) -> str:
    try:
        data = json.loads(response_text)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, ValueError):
        return response_text


def _call_api(endpoint: str, params: dict[str, Any]) -> str:
    url = f"{BASE_URL}{endpoint}"
    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: ExchangeRate.host API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_live(
    source: str | None = None,
    currencies: str | None = None,
) -> str:
    """Retrieve real-time exchange rates."""
    access_key = _get_access_key()
    params = _build_params(access_key, source=source, currencies=currencies)
    return _call_api("/live", params)


def get_historical(
    date: str,
    source: str | None = None,
    currencies: str | None = None,
) -> str:
    """Retrieve historical exchange rates for a specific date."""
    access_key = _get_access_key()
    params = _build_params(access_key, source=source, currencies=currencies)
    return _call_api("/historical", {**params, "date": date})


def convert_currency(
    from_: str,
    to: str,
    amount: float,
    date: str | None = None,
) -> str:
    """Convert an amount from one currency to another."""
    access_key = _get_access_key()
    params: dict[str, Any] = {"access_key": access_key, "from": from_, "to": to, "amount": amount}
    if date is not None:
        params["date"] = date
    return _call_api("/convert", params)


def get_timeframe(
    start_date: str,
    end_date: str,
    source: str | None = None,
    currencies: str | None = None,
) -> str:
    """Retrieve exchange rates for a date range (max 365 days)."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        start_date=start_date,
        end_date=end_date,
        source=source,
        currencies=currencies,
    )
    return _call_api("/timeframe", params)


def get_change(
    start_date: str,
    end_date: str,
    source: str | None = None,
    currencies: str | None = None,
) -> str:
    """Retrieve currency change/fluctuation between two dates."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        start_date=start_date,
        end_date=end_date,
        source=source,
        currencies=currencies,
    )
    return _call_api("/change", params)
