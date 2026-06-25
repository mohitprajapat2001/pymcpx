import os

from httpx import Response
import respx

from pymcpx.services.fixer import (
    FixerConvertTool,
    FixerHistoricalRatesTool,
    FixerLatestRatesTool,
    FixerSimulationEngine,
    FixerSymbolsTool,
    FixerToolkit,
)

# Mock access key for testing
os.environ["FIXER_ACCESS_KEY"] = "mock_key"


@respx.mock
def test_symbols_tool() -> None:
    tool = FixerSymbolsTool()
    assert tool.name == "fixer_symbols"

    request_mock = respx.get("https://data.fixer.io/api/symbols").mock(
        return_value=Response(
            200,
            json={
                "success": True,
                "symbols": {"USD": "United States Dollar", "EUR": "Euro"},
            },
        )
    )

    res = tool.run({})
    assert "USD" in res
    assert "Euro" in res
    assert request_mock.called


@respx.mock
def test_latest_rates_tool() -> None:
    tool = FixerLatestRatesTool()
    assert tool.name == "fixer_latest_rates"

    request_mock = respx.get("https://data.fixer.io/api/latest").mock(
        return_value=Response(
            200,
            json={
                "success": True,
                "base": "EUR",
                "date": "2025-09-15",
                "rates": {"USD": 1.23396, "GBP": 0.882047},
            },
        )
    )

    res = tool.run({"base": "EUR", "symbols": "USD,GBP"})
    assert "USD" in res
    assert "1.23396" in res
    assert request_mock.called


@respx.mock
def test_historical_rates_tool() -> None:
    tool = FixerHistoricalRatesTool()
    assert tool.name == "fixer_historical_rates"

    request_mock = respx.get("https://data.fixer.io/api/2013-12-24").mock(
        return_value=Response(
            200,
            json={
                "success": True,
                "historical": True,
                "date": "2013-12-24",
                "base": "GBP",
                "rates": {"USD": 1.636492},
            },
        )
    )

    res = tool.run({"date": "2013-12-24", "base": "GBP"})
    assert "2013-12-24" in res
    assert "1.636492" in res
    assert request_mock.called


@respx.mock
def test_convert_tool() -> None:
    tool = FixerConvertTool()
    assert tool.name == "fixer_convert"

    request_mock = respx.get("https://data.fixer.io/api/convert").mock(
        return_value=Response(
            200,
            json={
                "success": True,
                "query": {"from": "GBP", "to": "JPY", "amount": 25},
                "info": {"timestamp": 1519328414, "rate": 148.972231},
                "result": 3724.305775,
            },
        )
    )

    res = tool.run({"from_": "GBP", "to": "JPY", "amount": 25})
    assert "3724" in res
    assert request_mock.called


@respx.mock
def test_timeseries_tool() -> None:
    tool = FixerToolkit().get_tools()[4]
    assert tool.name == "fixer_timeseries"

    request_mock = respx.get("https://data.fixer.io/api/timeseries").mock(
        return_value=Response(
            200,
            json={
                "success": True,
                "timeseries": True,
                "start_date": "2012-05-01",
                "end_date": "2012-05-03",
                "base": "EUR",
                "rates": {
                    "2012-05-01": {"USD": 1.322891},
                    "2012-05-02": {"USD": 1.315066},
                },
            },
        )
    )

    res = tool.run({"start_date": "2012-05-01", "end_date": "2012-05-03"})
    assert "2012-05-01" in res
    assert "1.322891" in res
    assert request_mock.called


def test_toolkit() -> None:
    toolkit = FixerToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 6
    names = {t.name for t in tools}
    assert "fixer_symbols" in names
    assert "fixer_latest_rates" in names
    assert "fixer_historical_rates" in names
    assert "fixer_convert" in names
    assert "fixer_timeseries" in names
    assert "fixer_fluctuation" in names


def test_simulation_engine() -> None:
    engine = FixerSimulationEngine()
    engine.register(
        tool_name="fixer_latest_rates",
        input_match={"base": "EUR"},
        output='{"mocked": true}',
    )
    res = engine.run("fixer_latest_rates", {"base": "EUR"})
    assert res == '{"mocked": true}'
    assert engine.call_count == 1
