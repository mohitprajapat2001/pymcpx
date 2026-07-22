from httpx import Response
import respx

from pymcpx.services.cataas import (
    CataasSimulationEngine,
    CataasToolkit,
    CountCatsTool,
    GetCatByIdTool,
    GetCatByTagTool,
    GetRandomCatSayingTool,
    GetRandomCatTool,
    ListCatsTool,
    ListTagsTool,
)


@respx.mock
def test_list_tags_tool() -> None:
    tool = ListTagsTool()
    assert tool.name == "list_tags"

    respx.get("https://cataas.com/api/tags").mock(
        return_value=Response(200, json=["cute", "sleeping", "tabby", "orange"])
    )

    res = tool.run({"search": "cute", "limit": 5})
    assert "cute" in res
    assert "sleeping" not in res


@respx.mock
def test_list_cats_tool() -> None:
    tool = ListCatsTool()
    assert tool.name == "list_cats"

    respx.get("https://cataas.com/api/cats?limit=10&skip=0").mock(
        return_value=Response(
            200,
            json=[
                {"_id": "1", "tags": ["cute"], "mimetype": "image/jpeg", "createdAt": "2024-01-01"}
            ],
        )
    )

    res = tool.run({"limit": 10})
    assert "cute" in res


@respx.mock
def test_count_cats_tool() -> None:
    tool = CountCatsTool()
    assert tool.name == "count_cats"

    respx.get("https://cataas.com/api/count").mock(return_value=Response(200, json={"count": 1337}))

    res = tool.run({})
    assert "1337" in res


@respx.mock
def test_get_random_cat_tool() -> None:
    tool = GetRandomCatTool()
    assert tool.name == "get_random_cat"

    res = tool.run({"width": 200})
    assert res.startswith("https://cataas.com/cat")
    assert "width=200" in res


@respx.mock
def test_get_cat_by_id_tool() -> None:
    tool = GetCatByIdTool()
    assert tool.name == "get_cat_by_id"

    res = tool.run({"id": "abc123"})
    assert "abc123" in res


@respx.mock
def test_get_cat_by_tag_tool() -> None:
    tool = GetCatByTagTool()
    assert tool.name == "get_cat_by_tag"

    res = tool.run({"tag": "cute"})
    assert "/cat/cute" in res


@respx.mock
def test_get_random_cat_saying_tool() -> None:
    tool = GetRandomCatSayingTool()
    assert tool.name == "get_random_cat_saying"

    res = tool.run({"text": "hello"})
    assert "/cat/says/hello" in res


@respx.mock
def test_get_random_cat_with_json() -> None:
    tool = GetRandomCatTool()
    assert tool.name == "get_random_cat"

    respx.get("https://cataas.com/cat?json=true").mock(
        return_value=Response(
            200,
            json={
                "_id": "abc",
                "tags": ["cute"],
                "mimetype": "image/jpeg",
                "createdAt": "2024-01-01",
            },
        )
    )

    res = tool.run({"return_json": True})
    assert "abc" in res
    assert "cute" in res


def test_toolkit() -> None:
    toolkit = CataasToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 9
    names = {t.name for t in tools}
    assert "list_tags" in names
    assert "list_cats" in names
    assert "count_cats" in names
    assert "get_random_cat" in names
    assert "get_cat_by_id" in names
    assert "get_cat_by_tag" in names
    assert "get_random_cat_saying" in names
    assert "get_cat_by_id_saying" in names
    assert "get_random_cat_by_tag_saying" in names


def test_simulation_engine() -> None:
    engine = CataasSimulationEngine()
    engine.register(
        tool_name="list_tags",
        input_match={"search": "cute"},
        output='["cute"]',
    )
    res = engine.run("list_tags", {"search": "cute"})
    assert res == '["cute"]'
    assert engine.call_count == 1
