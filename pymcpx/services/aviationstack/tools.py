from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from pymcpx.services.aviationstack.SimulationEngine.models import (
    AviationstackAircraftTypesInput,
    AviationstackAirlinesInput,
    AviationstackAirplanesInput,
    AviationstackAirportsInput,
    AviationstackCitiesInput,
    AviationstackCountriesInput,
    AviationstackFlightsInput,
    AviationstackFutureFlightsInput,
    AviationstackRoutesInput,
    AviationstackTaxesInput,
    AviationstackTimetableInput,
)
from pymcpx.services.aviationstack.SimulationEngine.utils import (
    get_aircraft_types,
    get_airlines,
    get_airplanes,
    get_airports,
    get_cities,
    get_countries,
    get_flights,
    get_flights_future,
    get_routes,
    get_taxes,
    get_timetable,
)


class AviationstackFlightsTool(BaseTool):
    """Real-time and historical flight tracking."""

    name: str = "aviationstack_flights"
    description: str = (
        "Track real-time and historical flights worldwide. Supports filtering by "
        "flight date, status (scheduled/active/landed/cancelled/incident/diverted), "
        "departure/arrival airports (IATA/ICAO), airline, flight number, and delay ranges."
    )
    args_schema: type[BaseModel] = AviationstackFlightsInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_flights(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class AviationstackRoutesTool(BaseTool):
    """Airline route information."""

    name: str = "aviationstack_routes"
    description: str = (
        "Search airline routes by departure/arrival airports (IATA/ICAO), "
        "airline, or flight number."
    )
    args_schema: type[BaseModel] = AviationstackRoutesInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_routes(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class AviationstackAirportsTool(BaseTool):
    """Airport information lookup."""

    name: str = "aviationstack_airports"
    description: str = (
        "Search for airport information including name, IATA code, ICAO code, "
        "timezone, and geographic coordinates. Supports text search."
    )
    args_schema: type[BaseModel] = AviationstackAirportsInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_airports(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class AviationstackAirlinesTool(BaseTool):
    """Airline information lookup."""

    name: str = "aviationstack_airlines"
    description: str = (
        "Search for airline information including name, IATA code, ICAO code, "
        "and country of operation. Supports text search."
    )
    args_schema: type[BaseModel] = AviationstackAirlinesInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_airlines(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class AviationstackAirplanesTool(BaseTool):
    """Airplane/aircraft information lookup."""

    name: str = "aviationstack_airplanes"
    description: str = (
        "Search for airplane/aircraft information including registration number, "
        "manufacturer, model, and ICAO code. Supports text search."
    )
    args_schema: type[BaseModel] = AviationstackAirplanesInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_airplanes(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class AviationstackAircraftTypesTool(BaseTool):
    """Aircraft type code lookup."""

    name: str = "aviationstack_aircraft_types"
    description: str = "Search for aircraft type codes and descriptions. Supports text search."
    args_schema: type[BaseModel] = AviationstackAircraftTypesInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_aircraft_types(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class AviationstackTaxesTool(BaseTool):
    """Aviation tax information lookup."""

    name: str = "aviationstack_taxes"
    description: str = (
        "Search for aviation tax information including tax codes and amounts. Supports text search."
    )
    args_schema: type[BaseModel] = AviationstackTaxesInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_taxes(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class AviationstackCitiesTool(BaseTool):
    """City information lookup."""

    name: str = "aviationstack_cities"
    description: str = (
        "Search for city information including IATA code, timezone, and country. "
        "Supports text search."
    )
    args_schema: type[BaseModel] = AviationstackCitiesInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_cities(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class AviationstackCountriesTool(BaseTool):
    """Country information lookup."""

    name: str = "aviationstack_countries"
    description: str = (
        "Search for country information including name and ISO codes. Supports text search."
    )
    args_schema: type[BaseModel] = AviationstackCountriesInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_countries(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class AviationstackTimetableTool(BaseTool):
    """Real-time flight schedules for a specific airport."""

    name: str = "aviationstack_timetable"
    description: str = (
        "Retrieve real-time flight schedules (arrivals/departures) for a specific "
        "airport by IATA code. Requires iata_code and type (arrival/departure). "
        "Supports extensive filtering by terminal, delays, times, airline, and flight number."
    )
    args_schema: type[BaseModel] = AviationstackTimetableInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_timetable(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class AviationstackFlightsFutureTool(BaseTool):
    """Future flight schedules for a specific airport."""

    name: str = "aviationstack_flights_future"
    description: str = (
        "Retrieve future flight schedules for a specific airport by IATA code. "
        "Requires iata_code, type (arrival/departure), and date (YYYY-MM-DD). "
        "Optionally filter by airline or flight number."
    )
    args_schema: type[BaseModel] = AviationstackFutureFlightsInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_flights_future(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class AviationstackToolkit:
    """Convenience bundle that exposes all aviationstack tools."""

    def get_tools(self) -> list[BaseTool]:
        """Return a list of every aviationstack tool instance."""
        return [
            AviationstackFlightsTool(),
            AviationstackRoutesTool(),
            AviationstackAirportsTool(),
            AviationstackAirlinesTool(),
            AviationstackAirplanesTool(),
            AviationstackAircraftTypesTool(),
            AviationstackTaxesTool(),
            AviationstackCitiesTool(),
            AviationstackCountriesTool(),
            AviationstackTimetableTool(),
            AviationstackFlightsFutureTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    AviationstackFlightsTool(),
    AviationstackRoutesTool(),
    AviationstackAirportsTool(),
    AviationstackAirlinesTool(),
    AviationstackAirplanesTool(),
    AviationstackAircraftTypesTool(),
    AviationstackTaxesTool(),
    AviationstackCitiesTool(),
    AviationstackCountriesTool(),
    AviationstackTimetableTool(),
    AviationstackFlightsFutureTool(),
]
