import os

from httpx import Response
import respx

from pymcpx.services.numverify import (
    NumverifyCountriesTool,
    NumverifySimulationEngine,
    NumverifyToolkit,
    NumverifyValidateTool,
)

# Mock access key for testing
os.environ["NUMVERIFY_ACCESS_KEY"] = "mock_key"


@respx.mock
def test_validate_tool() -> None:
    tool = NumverifyValidateTool()
    assert tool.name == "numverify_validate"

    request_mock = respx.get("https://apilayer.net/api/validate").mock(
        return_value=Response(
            200,
            json={
                "valid": True,
                "number": "+14158586273",
                "local_format": "4158586273",
                "international_format": "+14158586273",
                "country_prefix": "+1",
                "country_code": "US",
                "country_name": "United States of America",
                "location": "Novato",
                "carrier": "AT&T Mobility LLC",
                "line_type": "mobile",
            },
        )
    )

    res = tool.run({"number": "+14158586273"})
    assert "United States" in res
    assert "AT&T" in res
    assert "mobile" in res
    assert request_mock.called


@respx.mock
def test_countries_tool() -> None:
    tool = NumverifyCountriesTool()
    assert tool.name == "numverify_countries"

    request_mock = respx.get("https://apilayer.net/api/countries").mock(
        return_value=Response(
            200,
            json={
                "US": {"country_name": "United States of America", "dialling_code": "+1"},
                "IN": {"country_name": "India", "dialling_code": "+91"},
            },
        )
    )

    res = tool.run({})
    assert "United States" in res
    assert "India" in res
    assert request_mock.called


def test_toolkit() -> None:
    toolkit = NumverifyToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 2
    names = {t.name for t in tools}
    assert "numverify_validate" in names
    assert "numverify_countries" in names


def test_simulation_engine() -> None:
    engine = NumverifySimulationEngine()
    engine.register(
        tool_name="numverify_validate",
        input_match={"number": "+14158586273"},
        output='{"mocked": true}',
    )
    res = engine.run("numverify_validate", {"number": "+14158586273"})
    assert res == '{"mocked": true}'
    assert engine.call_count == 1
