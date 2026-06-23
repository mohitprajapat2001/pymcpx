from datetime import datetime
from zoneinfo import ZoneInfo

from pymcpx.services.datetime import (
    ConvertTimezoneTool,
    DatetimeToolkit,
    DatetimeToTimestampTool,
    GetCurrentTimeTool,
    GetDayOfWeekTool,
    TimestampToDatetimeTool,
)
from pymcpx.services.datetime.SimulationEngine import DatetimeSimulationEngine


def test_get_current_time_tool() -> None:
    tool = GetCurrentTimeTool()
    assert tool.name == "get_current_time"
    res = tool.run({"timezone": "UTC", "format": "%Y-%m-%d"})
    expected = datetime.now(ZoneInfo("UTC")).strftime("%Y-%m-%d")
    assert res == expected


def test_get_current_time_tool_invalid_tz() -> None:
    tool = GetCurrentTimeTool()
    res = tool.run({"timezone": "Invalid/Timezone"})
    assert "Error:" in res


def test_convert_timezone_tool() -> None:
    tool = ConvertTimezoneTool()
    assert tool.name == "convert_timezone"
    res = tool.run(
        {
            "datetime_str": "2026-06-24T12:00:00",
            "from_tz": "America/New_York",
            "to_tz": "UTC",
        }
    )
    # 2026-06-24T12:00:00-04:00 is America/New_York (EDT)
    # converted to UTC is 16:00:00Z
    assert "2026-06-24T16:00:00+00:00" in res or "2026-06-24T16:00:00Z" in res


def test_get_day_of_week_tool() -> None:
    tool = GetDayOfWeekTool()
    assert tool.name == "get_day_of_week"
    # June 24, 2026 is a Wednesday
    assert tool.run({"date_str": "2026-06-24"}) == "Wednesday"


def test_timestamp_to_datetime_tool() -> None:
    tool = TimestampToDatetimeTool()
    assert tool.name == "timestamp_to_datetime"
    # 1782316800 is Wed Jun 24 2026 16:00:00 UTC
    res = tool.run({"timestamp": 1782316800.0, "timezone": "UTC", "format": "%Y-%m-%d %H:%M:%S"})
    assert res == "2026-06-24 16:00:00"


def test_datetime_to_timestamp_tool() -> None:
    tool = DatetimeToTimestampTool()
    assert tool.name == "datetime_to_timestamp"
    res = tool.run({"datetime_str": "2026-06-24T16:00:00", "timezone": "UTC"})
    assert float(res) == 1782316800.0


def test_datetime_toolkit() -> None:
    toolkit = DatetimeToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 5
    names = {t.name for t in tools}
    assert "get_current_time" in names
    assert "convert_timezone" in names


def test_datetime_simulation_engine() -> None:
    engine = DatetimeSimulationEngine()
    engine.register(
        tool_name="get_current_time",
        input_match={"timezone": "UTC"},
        output="2026-06-24T12:00:00Z",
    )

    res = engine.run("get_current_time", {"timezone": "UTC"})
    assert res == "2026-06-24T12:00:00Z"
    assert engine.call_count == 1
    assert engine.history[0].tool_name == "get_current_time"

    # Non-matched fallback
    fallback_res = engine.run(
        "convert_timezone",
        {
            "datetime_str": "2026-06-24T12:00:00",
            "from_tz": "America/New_York",
            "to_tz": "UTC",
        },
    )
    assert "2026-06-24T16:00:00" in fallback_res
    assert engine.call_count == 2
