import os

from httpx import Response
import respx

from pymcpx.services.marketstack import (
    MarketstackEodTool,
    MarketstackIntradayTool,
    MarketstackRealtimePriceTool,
    MarketstackSimulationEngine,
    MarketstackToolkit,
)

# Mock access key for testing
os.environ["MARKETSTACK_ACCESS_KEY"] = "mock_key"


@respx.mock
def test_eod_tool() -> None:
    tool = MarketstackEodTool()
    assert tool.name == "marketstack_eod"

    request_mock = respx.get("https://api.marketstack.com/v2/eod").mock(
        return_value=Response(200, json={"data": [{"symbol": "AAPL", "close": 150.0}]})
    )

    res = tool.run({"symbols": "AAPL"})
    assert "AAPL" in res
    assert "150" in res
    assert request_mock.called


@respx.mock
def test_intraday_tool_latest() -> None:
    tool = MarketstackIntradayTool()
    assert tool.name == "marketstack_intraday"

    request_mock = respx.get("https://api.marketstack.com/v2/intraday/latest").mock(
        return_value=Response(200, json={"data": [{"symbol": "AAPL", "last": 150.5}]})
    )

    res = tool.run({"symbols": "AAPL", "latest": True})
    assert "AAPL" in res
    assert "150.5" in res
    assert request_mock.called


@respx.mock
def test_realtime_price_tool() -> None:
    tool = MarketstackRealtimePriceTool()
    assert tool.name == "marketstack_realtime_price"

    request_mock = respx.get("https://api.marketstack.com/v2/stockprice").mock(
        return_value=Response(200, json={"data": [{"ticker": "AAPL", "price": "150.0"}]})
    )

    res = tool.run({"ticker": "AAPL"})
    assert "AAPL" in res
    assert "150.0" in res
    assert request_mock.called


def test_toolkit() -> None:
    toolkit = MarketstackToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 18
    names = {t.name for t in tools}
    assert "marketstack_eod" in names
    assert "marketstack_intraday" in names
    assert "marketstack_realtime_price" in names
    assert "marketstack_edgar_facts" in names


def test_simulation_engine() -> None:
    engine = MarketstackSimulationEngine()
    engine.register(
        tool_name="marketstack_realtime_price",
        input_match={"ticker": "AAPL"},
        output='{"mocked": true}',
    )
    res = engine.run("marketstack_realtime_price", {"ticker": "AAPL"})
    assert res == '{"mocked": true}'
    assert engine.call_count == 1
