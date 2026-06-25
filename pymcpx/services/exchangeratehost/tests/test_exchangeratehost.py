import os

from httpx import Response
import respx

from pymcpx.services.exchangeratehost import (
    ExchangeratehostChangeTool,
    ExchangeratehostConvertTool,
    ExchangeratehostHistoricalTool,
    ExchangeratehostLiveTool,
    ExchangeratehostSimulationEngine,
    ExchangeratehostTimeframeTool,
    ExchangeratehostToolkit,
)

os.environ["EXCHANGERATEHOST_ACCESS_KEY"] = "mock_key"

MOCK_LIVE = {
    "success": True,
    "timestamp": 1698739200,
    "source": "USD",
    "quotes": {"USDGBP": 0.7701, "USDEUR": 0.8123},
}

MOCK_HISTORICAL = {
    "success": True,
    "historical": True,
    "date": "2020-01-01",
    "timestamp": 1577836800,
    "source": "USD",
    "quotes": {"USDGBP": 0.7321, "USDEUR": 0.8159},
}

MOCK_CONVERT = {
    "success": True,
    "timestamp": 1698739200,
    "query": {"from": "USD", "to": "GBP", "amount": 100},
    "info": {"timestamp": 1698739200, "rate": 0.7701},
    "result": 77.01,
}

MOCK_TIMEFRAME = {
    "success": True,
    "timeframe": True,
    "start_date": "2020-01-01",
    "end_date": "2020-01-03",
    "source": "USD",
    "rates": {
        "2020-01-01": {"USDGBP": 0.7701},
        "2020-01-02": {"USDGBP": 0.7720},
    },
}


@respx.mock
def test_live_tool() -> None:
    tool = ExchangeratehostLiveTool()
    assert tool.name == "exchangeratehost_live"

    request_mock = respx.get("https://api.exchangerate.host/live").mock(
        return_value=Response(200, json=MOCK_LIVE)
    )

    res = tool.run({})
    assert "USDGBP" in res
    assert request_mock.called


@respx.mock
def test_live_tool_with_params() -> None:
    tool = ExchangeratehostLiveTool()

    request_mock = respx.get("https://api.exchangerate.host/live").mock(
        return_value=Response(200, json=MOCK_LIVE)
    )

    tool.run({"source": "EUR", "currencies": "USD,GBP"})
    assert request_mock.called
    query = request_mock.calls[0].request.url.query.decode("utf-8")
    assert "source=EUR" in query
    assert "currencies=USD%2CGBP" in query


@respx.mock
def test_historical_tool() -> None:
    tool = ExchangeratehostHistoricalTool()
    assert tool.name == "exchangeratehost_historical"

    request_mock = respx.get("https://api.exchangerate.host/historical").mock(
        return_value=Response(200, json=MOCK_HISTORICAL)
    )

    res = tool.run({"date": "2020-01-01"})
    assert "USDGBP" in res
    assert request_mock.called
    assert "date=2020-01-01" in request_mock.calls[0].request.url.query.decode("utf-8")


@respx.mock
def test_convert_tool() -> None:
    tool = ExchangeratehostConvertTool()
    assert tool.name == "exchangeratehost_convert"

    request_mock = respx.get("https://api.exchangerate.host/convert").mock(
        return_value=Response(200, json=MOCK_CONVERT)
    )

    res = tool.run({"from_": "USD", "to": "GBP", "amount": 100})
    assert "77.01" in res
    assert request_mock.called
    query = request_mock.calls[0].request.url.query.decode("utf-8")
    assert "from=USD" in query
    assert "to=GBP" in query
    assert "amount=100" in query


@respx.mock
def test_timeframe_tool() -> None:
    tool = ExchangeratehostTimeframeTool()
    assert tool.name == "exchangeratehost_timeframe"

    request_mock = respx.get("https://api.exchangerate.host/timeframe").mock(
        return_value=Response(200, json=MOCK_TIMEFRAME)
    )

    res = tool.run({"start_date": "2020-01-01", "end_date": "2020-01-03"})
    assert "timeframe" in res
    assert request_mock.called
    query = request_mock.calls[0].request.url.query.decode("utf-8")
    assert "start_date=2020-01-01" in query
    assert "end_date=2020-01-03" in query


@respx.mock
def test_change_tool() -> None:
    tool = ExchangeratehostChangeTool()
    assert tool.name == "exchangeratehost_change"

    request_mock = respx.get("https://api.exchangerate.host/change").mock(
        return_value=Response(
            200,
            json={
                "success": True,
                "change": True,
                "start_date": "2020-01-01",
                "end_date": "2020-01-03",
                "source": "USD",
                "rates": {
                    "USDGBP": {
                        "start_rate": 0.7701,
                        "end_rate": 0.7695,
                        "change": -0.0006,
                        "change_pct": -0.07792,
                    }
                },
            },
        )
    )

    res = tool.run({"start_date": "2020-01-01", "end_date": "2020-01-03"})
    assert "change" in res
    assert request_mock.called
    query = request_mock.calls[0].request.url.query.decode("utf-8")
    assert "start_date=2020-01-01" in query
    assert "end_date=2020-01-03" in query


def test_toolkit() -> None:
    toolkit = ExchangeratehostToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 5
    names = {t.name for t in tools}
    expected = {
        "exchangeratehost_live",
        "exchangeratehost_historical",
        "exchangeratehost_convert",
        "exchangeratehost_timeframe",
        "exchangeratehost_change",
    }
    assert names == expected


def test_simulation_engine() -> None:
    engine = ExchangeratehostSimulationEngine()
    engine.register(
        tool_name="exchangeratehost_live",
        input_match={"source": "USD"},
        output='{"mocked": true}',
    )
    res = engine.run("exchangeratehost_live", {"source": "USD"})
    assert res == '{"mocked": true}'
    assert engine.call_count == 1
