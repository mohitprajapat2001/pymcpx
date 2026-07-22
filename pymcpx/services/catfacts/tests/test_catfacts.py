from httpx import Response
import respx

from pymcpx.services.catfacts import (
    CatfactsSimulationEngine,
    CatfactsToolkit,
    GetBreedsTool,
    GetFactsTool,
    GetRandomFactTool,
)


@respx.mock
def test_get_breeds_tool() -> None:
    tool = GetBreedsTool()
    assert tool.name == "get_breeds"

    request_mock = respx.get("https://catfact.ninja/breeds").mock(
        return_value=Response(
            200,
            json=[
                {
                    "breed": "Abyssinian",
                    "country": "Ethiopia",
                    "origin": "Natural",
                    "coat": "Short",
                    "pattern": "Ticked",
                }
            ],
        )
    )

    res = tool.run({"limit": 1})
    assert "Abyssinian" in res
    assert "Ethiopia" in res
    assert request_mock.called


@respx.mock
def test_get_random_fact_tool() -> None:
    tool = GetRandomFactTool()
    assert tool.name == "get_random_fact"

    request_mock = respx.get("https://catfact.ninja/fact").mock(
        return_value=Response(
            200,
            json={"fact": "Cats are awesome.", "length": 16},
        )
    )

    res = tool.run({"max_length": 50})
    assert "Cats are awesome" in res
    assert "16" in res
    assert request_mock.called


@respx.mock
def test_get_facts_tool() -> None:
    tool = GetFactsTool()
    assert tool.name == "get_facts"

    request_mock = respx.get("https://catfact.ninja/facts").mock(
        return_value=Response(
            200,
            json=[
                {"fact": "Cats sleep a lot.", "length": 18},
                {"fact": "Cats are cute.", "length": 15},
            ],
        )
    )

    res = tool.run({"limit": 2, "max_length": 100})
    assert "Cats sleep a lot" in res
    assert "Cats are cute" in res
    assert request_mock.called


def test_toolkit() -> None:
    toolkit = CatfactsToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 3
    names = {t.name for t in tools}
    assert "get_breeds" in names
    assert "get_random_fact" in names
    assert "get_facts" in names


def test_simulation_engine() -> None:
    engine = CatfactsSimulationEngine()
    engine.register(
        tool_name="get_random_fact",
        input_match={"max_length": 50},
        output='{"mocked": true}',
    )
    res = engine.run("get_random_fact", {"max_length": 50})
    assert res == '{"mocked": true}'
    assert engine.call_count == 1
