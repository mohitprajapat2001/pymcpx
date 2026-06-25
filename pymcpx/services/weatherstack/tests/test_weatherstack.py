import os

from httpx import Response
import respx

from pymcpx.services.weatherstack import (
    WeatherstackCurrentTool,
    WeatherstackForecastTool,
    WeatherstackSimulationEngine,
    WeatherstackToolkit,
)

# Mock access key for testing
os.environ["WEATHERSTACK_ACCESS_KEY"] = "mock_key"


@respx.mock
def test_current_tool() -> None:
    tool = WeatherstackCurrentTool()
    assert tool.name == "weatherstack_current"

    request_mock = respx.get("https://api.weatherstack.com/current").mock(
        return_value=Response(
            200,
            json={
                "location": {"name": "New York"},
                "current": {"temperature": 22},
            },
        )
    )

    res = tool.run({"query": "New York"})
    assert "New York" in res
    assert "22" in res
    assert request_mock.called


@respx.mock
def test_forecast_tool() -> None:
    tool = WeatherstackForecastTool()
    assert tool.name == "weatherstack_forecast"

    request_mock = respx.get("https://api.weatherstack.com/forecast").mock(
        return_value=Response(
            200,
            json={
                "location": {"name": "London"},
                "forecast": {"2025-06-01": {"mintemp": 15}},
            },
        )
    )

    res = tool.run({"query": "London", "forecast_days": 3})
    assert "London" in res
    assert "15" in res
    assert request_mock.called


def test_toolkit() -> None:
    toolkit = WeatherstackToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 6
    names = {t.name for t in tools}
    assert "weatherstack_current" in names
    assert "weatherstack_forecast" in names
    assert "weatherstack_historical" in names
    assert "weatherstack_marine" in names
    assert "weatherstack_historical_marine" in names
    assert "weatherstack_autocomplete" in names


def test_simulation_engine() -> None:
    engine = WeatherstackSimulationEngine()
    engine.register(
        tool_name="weatherstack_current",
        input_match={"query": "New York"},
        output='{"mocked": true}',
    )
    res = engine.run("weatherstack_current", {"query": "New York"})
    assert res == '{"mocked": true}'
    assert engine.call_count == 1
