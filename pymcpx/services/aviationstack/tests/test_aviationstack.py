import os

from httpx import Response
import respx

from pymcpx.services.aviationstack import (
    AviationstackAirlinesTool,
    AviationstackAirportsTool,
    AviationstackFlightsFutureTool,
    AviationstackFlightsTool,
    AviationstackRoutesTool,
    AviationstackSimulationEngine,
    AviationstackTimetableTool,
    AviationstackToolkit,
)

os.environ["AVIATIONSTACK_ACCESS_KEY"] = "mock_key"


@respx.mock
def test_flights_tool() -> None:
    tool = AviationstackFlightsTool()
    assert tool.name == "aviationstack_flights"

    request_mock = respx.get("https://api.aviationstack.com/v1/flights").mock(
        return_value=Response(
            200,
            json={
                "data": [
                    {
                        "flight_date": "2025-09-15",
                        "flight_status": "active",
                        "departure": {"airport": "JFK", "iata": "JFK"},
                        "arrival": {"airport": "LAX", "iata": "LAX"},
                        "airline": {"name": "American Airlines", "iata": "AA"},
                        "flight": {"number": "100", "iata": "AA100"},
                    }
                ]
            },
        )
    )

    res = tool.run({"flight_date": "2025-09-15", "dep_iata": "JFK"})
    assert "American Airlines" in res
    assert "AA100" in res
    assert request_mock.called


@respx.mock
def test_routes_tool() -> None:
    tool = AviationstackRoutesTool()
    assert tool.name == "aviationstack_routes"

    request_mock = respx.get("https://api.aviationstack.com/v1/routes").mock(
        return_value=Response(
            200,
            json={
                "data": [
                    {
                        "departure": {"airport": "JFK", "iata": "JFK"},
                        "arrival": {"airport": "LHR", "iata": "LHR"},
                        "airline": {"name": "British Airways", "iata": "BA"},
                    }
                ]
            },
        )
    )

    res = tool.run({"dep_iata": "JFK", "arr_iata": "LHR"})
    assert "British Airways" in res
    assert request_mock.called


@respx.mock
def test_airports_tool() -> None:
    tool = AviationstackAirportsTool()
    assert tool.name == "aviationstack_airports"

    request_mock = respx.get("https://api.aviationstack.com/v1/airports").mock(
        return_value=Response(
            200,
            json={
                "data": [
                    {
                        "airport_name": "John F Kennedy International",
                        "iata_code": "JFK",
                        "icao_code": "KJFK",
                        "country_name": "United States",
                    }
                ]
            },
        )
    )

    res = tool.run({"search": "JFK"})
    assert "John F Kennedy" in res
    assert request_mock.called


@respx.mock
def test_airlines_tool() -> None:
    tool = AviationstackAirlinesTool()
    assert tool.name == "aviationstack_airlines"

    request_mock = respx.get("https://api.aviationstack.com/v1/airlines").mock(
        return_value=Response(
            200,
            json={
                "data": [
                    {
                        "airline_name": "American Airlines",
                        "iata_code": "AA",
                        "icao_code": "AAL",
                    }
                ]
            },
        )
    )

    res = tool.run({"search": "American"})
    assert "American Airlines" in res
    assert request_mock.called


@respx.mock
def test_timetable_tool() -> None:
    tool = AviationstackTimetableTool()
    assert tool.name == "aviationstack_timetable"

    request_mock = respx.get("https://api.aviationstack.com/v1/timetable").mock(
        return_value=Response(
            200,
            json={
                "data": [
                    {
                        "flight": {"iata": "AA100"},
                        "departure": {"airport": "JFK"},
                        "arrival": {"airport": "LAX"},
                    }
                ]
            },
        )
    )

    res = tool.run({"iata_code": "JFK", "type": "departure"})
    assert "AA100" in res
    assert request_mock.called


@respx.mock
def test_flights_future_tool() -> None:
    tool = AviationstackFlightsFutureTool()
    assert tool.name == "aviationstack_flights_future"

    request_mock = respx.get("https://api.aviationstack.com/v1/flightsFuture").mock(
        return_value=Response(
            200,
            json={
                "data": [
                    {
                        "flight": {"iata": "BA178"},
                        "departure": {"airport": "LHR"},
                        "arrival": {"airport": "JFK"},
                    }
                ]
            },
        )
    )

    res = tool.run({"iata_code": "LHR", "type": "departure", "date": "2025-12-25"})
    assert "BA178" in res
    assert request_mock.called


def test_toolkit() -> None:
    toolkit = AviationstackToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 11
    names = {t.name for t in tools}
    expected = {
        "aviationstack_flights",
        "aviationstack_routes",
        "aviationstack_airports",
        "aviationstack_airlines",
        "aviationstack_airplanes",
        "aviationstack_aircraft_types",
        "aviationstack_taxes",
        "aviationstack_cities",
        "aviationstack_countries",
        "aviationstack_timetable",
        "aviationstack_flights_future",
    }
    assert names == expected


def test_simulation_engine() -> None:
    engine = AviationstackSimulationEngine()
    engine.register(
        tool_name="aviationstack_flights",
        input_match={"dep_iata": "JFK"},
        output='{"mocked": true}',
    )
    res = engine.run("aviationstack_flights", {"dep_iata": "JFK"})
    assert res == '{"mocked": true}'
    assert engine.call_count == 1
