from __future__ import annotations

import json
import os
from typing import Any

import httpx

BASE_URL = "https://api.aviationstack.com/v1"


def _get_access_key() -> str:
    """Retrieve the Aviationstack API access key from the environment."""
    key = os.environ.get("AVIATIONSTACK_ACCESS_KEY")
    if not key:
        raise ValueError(
            "AVIATIONSTACK_ACCESS_KEY environment variable is not set. "
            "Please set it to your Aviationstack API access key."
        )
    return key


def _build_params(access_key: str, **kwargs: Any) -> dict[str, Any]:
    """Build query parameters dict, dropping None values."""
    params: dict[str, Any] = {"access_key": access_key}
    for k, v in kwargs.items():
        if v is not None:
            params[k] = v
    return params


def _format_response(response_text: str) -> str:
    """Pretty-print a JSON response, or return raw text if it's not JSON."""
    try:
        data = json.loads(response_text)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except (json.JSONDecodeError, ValueError):
        return response_text


def _call_api(endpoint: str, params: dict[str, Any]) -> str:
    """Make a GET request to the Aviationstack API and return formatted output."""
    url = f"{BASE_URL}/{endpoint}"
    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=30)

    if response.status_code != 200:
        return f"Error: Aviationstack API returned HTTP {response.status_code} — {response.text}"

    return _format_response(response.text)


def get_flights(
    limit: int | None = None,
    offset: int | None = None,
    flight_date: str | None = None,
    flight_status: str | None = None,
    dep_iata: str | None = None,
    arr_iata: str | None = None,
    dep_icao: str | None = None,
    arr_icao: str | None = None,
    airline_name: str | None = None,
    airline_iata: str | None = None,
    airline_icao: str | None = None,
    flight_number: str | None = None,
    flight_iata: str | None = None,
    flight_icao: str | None = None,
    min_delay_dep: int | None = None,
    min_delay_arr: int | None = None,
    max_delay_dep: int | None = None,
    max_delay_arr: int | None = None,
    arr_scheduled_time_arr: str | None = None,
    dep_scheduled_time_dep: str | None = None,
) -> str:
    """Retrieve real-time and historical flight data."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        limit=limit,
        offset=offset,
        flight_date=flight_date,
        flight_status=flight_status,
        dep_iata=dep_iata,
        arr_iata=arr_iata,
        dep_icao=dep_icao,
        arr_icao=arr_icao,
        airline_name=airline_name,
        airline_iata=airline_iata,
        airline_icao=airline_icao,
        flight_number=flight_number,
        flight_iata=flight_iata,
        flight_icao=flight_icao,
        min_delay_dep=min_delay_dep,
        min_delay_arr=min_delay_arr,
        max_delay_dep=max_delay_dep,
        max_delay_arr=max_delay_arr,
        arr_scheduled_time_arr=arr_scheduled_time_arr,
        dep_scheduled_time_dep=dep_scheduled_time_dep,
    )
    return _call_api("flights", params)


def get_routes(
    limit: int | None = None,
    offset: int | None = None,
    dep_iata: str | None = None,
    arr_iata: str | None = None,
    dep_icao: str | None = None,
    arr_icao: str | None = None,
    airline_iata: str | None = None,
    airline_icao: str | None = None,
    flight_number: str | None = None,
) -> str:
    """Retrieve airline route information."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        limit=limit,
        offset=offset,
        dep_iata=dep_iata,
        arr_iata=arr_iata,
        dep_icao=dep_icao,
        arr_icao=arr_icao,
        airline_iata=airline_iata,
        airline_icao=airline_icao,
        flight_number=flight_number,
    )
    return _call_api("routes", params)


def list_endpoint(
    endpoint: str, limit: int | None = None, offset: int | None = None, search: str | None = None
) -> str:
    """Generic function for list-type endpoints with optional search."""
    access_key = _get_access_key()
    params = _build_params(access_key, limit=limit, offset=offset, search=search)
    return _call_api(endpoint, params)


def get_airports(
    limit: int | None = None, offset: int | None = None, search: str | None = None
) -> str:
    """Retrieve airport information."""
    return list_endpoint("airports", limit=limit, offset=offset, search=search)


def get_airlines(
    limit: int | None = None, offset: int | None = None, search: str | None = None
) -> str:
    """Retrieve airline information."""
    return list_endpoint("airlines", limit=limit, offset=offset, search=search)


def get_airplanes(
    limit: int | None = None, offset: int | None = None, search: str | None = None
) -> str:
    """Retrieve airplane/aircraft information."""
    return list_endpoint("airplanes", limit=limit, offset=offset, search=search)


def get_aircraft_types(
    limit: int | None = None, offset: int | None = None, search: str | None = None
) -> str:
    """Retrieve aircraft type codes."""
    return list_endpoint("aircraft_types", limit=limit, offset=offset, search=search)


def get_taxes(
    limit: int | None = None, offset: int | None = None, search: str | None = None
) -> str:
    """Retrieve aviation tax information."""
    return list_endpoint("taxes", limit=limit, offset=offset, search=search)


def get_cities(
    limit: int | None = None, offset: int | None = None, search: str | None = None
) -> str:
    """Retrieve city information."""
    return list_endpoint("cities", limit=limit, offset=offset, search=search)


def get_countries(
    limit: int | None = None, offset: int | None = None, search: str | None = None
) -> str:
    """Retrieve country information."""
    return list_endpoint("countries", limit=limit, offset=offset, search=search)


def get_timetable(
    iata_code: str,
    type: str,
    status: str | None = None,
    dep_terminal: str | None = None,
    dep_delay: int | None = None,
    dep_sch_time: str | None = None,
    dep_est_time: str | None = None,
    dep_act_time: str | None = None,
    dep_est_runway: str | None = None,
    dep_act_runway: str | None = None,
    arr_terminal: str | None = None,
    arr_delay: int | None = None,
    arr_sch_time: str | None = None,
    arr_est_time: str | None = None,
    arr_act_time: str | None = None,
    arr_est_runway: str | None = None,
    arr_act_runway: str | None = None,
    airline_name: str | None = None,
    airline_iata: str | None = None,
    airline_icao: str | None = None,
    flight_number: str | None = None,
    flight_iata: str | None = None,
    flight_icao: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> str:
    """Retrieve real-time flight schedules for a specific airport."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        iataCode=iata_code,
        type=type,
        status=status,
        dep_terminal=dep_terminal,
        dep_delay=dep_delay,
        dep_schTime=dep_sch_time,
        dep_estTime=dep_est_time,
        dep_actTime=dep_act_time,
        dep_estRunway=dep_est_runway,
        dep_actRunway=dep_act_runway,
        arr_terminal=arr_terminal,
        arr_delay=arr_delay,
        arr_schTime=arr_sch_time,
        arr_estTime=arr_est_time,
        arr_actTime=arr_act_time,
        arr_estRunway=arr_est_runway,
        arr_actRunway=arr_act_runway,
        airline_name=airline_name,
        airline_iata=airline_iata,
        airline_icao=airline_icao,
        flight_number=flight_number,
        flight_iata=flight_iata,
        flight_icao=flight_icao,
        limit=limit,
        offset=offset,
    )
    return _call_api("timetable", params)


def get_flights_future(
    iata_code: str,
    type: str,
    date: str,
    airline_iata: str | None = None,
    airline_icao: str | None = None,
    flight_number: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
) -> str:
    """Retrieve future flight schedules for a specific airport."""
    access_key = _get_access_key()
    params = _build_params(
        access_key,
        iataCode=iata_code,
        type=type,
        date=date,
        airline_iata=airline_iata,
        airline_icao=airline_icao,
        flight_number=flight_number,
        limit=limit,
        offset=offset,
    )
    return _call_api("flightsFuture", params)
