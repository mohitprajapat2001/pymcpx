from __future__ import annotations

import json
import os
from typing import Any

import httpx

V2_BASE_URL = "https://app.zenserp.com/api/v2"
V1_BASE_URL = "https://app.zenserp.com/api/v1"


def _get_api_key() -> str:
    key = os.environ.get("ZENSERP_API_KEY")
    if not key:
        raise ValueError(
            "ZENSERP_API_KEY environment variable is not set. "
            "Please set it to your Zenserp API key."
        )
    return key


def _format_response(response_text: str) -> str:
    try:
        data = json.loads(response_text)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, ValueError):
        return response_text


def _call_api(url: str, params: dict[str, Any]) -> str:
    api_key = _get_api_key()
    headers = {"apikey": api_key}
    with httpx.Client() as client:
        response = client.get(url, params=params, headers=headers, timeout=30)

    if response.status_code != 200:
        return f"Error: Zenserp API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def search(**params: Any) -> str:
    """Search Google/Bing/Yandex/YouTube via Zenserp."""
    return _call_api(f"{V2_BASE_URL}/search", params)


def get_shopping_product(**params: Any) -> str:
    """Retrieve shopping product page details."""
    return _call_api(f"{V1_BASE_URL}/shopping", params)


def get_trends(**params: Any) -> str:
    """Retrieve Google Trends data."""
    final_params: dict[str, Any] = {}
    for k, v in params.items():
        if k == "keywords":
            final_params["keyword[]"] = v
        elif v is not None:
            final_params[k] = v
    return _call_api(f"{V1_BASE_URL}/trends", final_params)


def get_trending(**params: Any) -> str:
    """Retrieve Google Trending searches."""
    return _call_api(f"{V1_BASE_URL}/trends/trending", {k: v for k, v in params.items() if v is not None})


def get_status(**params: Any) -> str:
    """Check Zenserp account status and remaining requests."""
    return _call_api(f"{V2_BASE_URL}/status", params)


def get_languages(**params: Any) -> str:
    """List supported Google interface languages."""
    return _call_api(f"{V2_BASE_URL}/hl", params)


def get_countries(**params: Any) -> str:
    """List supported Google country codes."""
    return _call_api(f"{V2_BASE_URL}/gl", params)


def get_locations(**params: Any) -> str:
    """List supported geo locations."""
    return _call_api(f"{V2_BASE_URL}/locations", params)


def get_search_engines(**params: Any) -> str:
    """List supported search engines."""
    return _call_api(f"{V2_BASE_URL}/search_engines", params)
