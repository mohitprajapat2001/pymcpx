import os

from httpx import Response
import respx

from pymcpx.services.zenserp import (
    ZenserpBingSearchTool,
    ZenserpCountriesTool,
    ZenserpImageSearchTool,
    ZenserpLanguagesTool,
    ZenserpLocationsTool,
    ZenserpNewsSearchTool,
    ZenserpSearchEnginesTool,
    ZenserpSearchTool,
    ZenserpShoppingProductTool,
    ZenserpShoppingSearchTool,
    ZenserpSimulationEngine,
    ZenserpStatusTool,
    ZenserpToolkit,
    ZenserpTrendingTool,
    ZenserpTrendsTool,
    ZenserpVideoSearchTool,
    ZenserpYouTubeSearchTool,
)

os.environ["ZENSERP_API_KEY"] = "mock_key"

MOCK_SEARCH_RESPONSE = {
    "query": {"q": "test", "search_engine": "google.com"},
    "organic": [{"title": "Test Result", "url": "https://example.com", "snippet": "Test snippet"}],
    "total_results": 1,
}


@respx.mock
def test_search_tool() -> None:
    tool = ZenserpSearchTool()
    assert tool.name == "zenserp_search"

    request_mock = respx.get("https://app.zenserp.com/api/v2/search").mock(
        return_value=Response(200, json=MOCK_SEARCH_RESPONSE)
    )

    res = tool.run({"q": "test"})
    assert "Test Result" in res
    assert request_mock.called


@respx.mock
def test_image_search_tool() -> None:
    tool = ZenserpImageSearchTool()
    assert tool.name == "zenserp_image_search"

    request_mock = respx.get("https://app.zenserp.com/api/v2/search").mock(
        return_value=Response(200, json=MOCK_SEARCH_RESPONSE)
    )

    res = tool.run({"q": "cats"})
    assert "Test Result" in res
    assert request_mock.called
    assert "tbm=isch" in request_mock.calls[0].request.url.query.decode("utf-8")


@respx.mock
def test_video_search_tool() -> None:
    tool = ZenserpVideoSearchTool()
    assert tool.name == "zenserp_video_search"

    request_mock = respx.get("https://app.zenserp.com/api/v2/search").mock(
        return_value=Response(200, json=MOCK_SEARCH_RESPONSE)
    )

    tool.run({"q": "test video"})
    assert request_mock.called
    assert "tbm=vid" in request_mock.calls[0].request.url.query.decode("utf-8")


@respx.mock
def test_news_search_tool() -> None:
    tool = ZenserpNewsSearchTool()
    assert tool.name == "zenserp_news_search"

    request_mock = respx.get("https://app.zenserp.com/api/v2/search").mock(
        return_value=Response(200, json=MOCK_SEARCH_RESPONSE)
    )

    tool.run({"q": "latest news"})
    assert request_mock.called
    assert "tbm=nws" in request_mock.calls[0].request.url.query.decode("utf-8")


@respx.mock
def test_shopping_search_tool() -> None:
    tool = ZenserpShoppingSearchTool()
    assert tool.name == "zenserp_shopping_search"

    request_mock = respx.get("https://app.zenserp.com/api/v2/search").mock(
        return_value=Response(200, json=MOCK_SEARCH_RESPONSE)
    )

    tool.run({"q": "laptop"})
    assert request_mock.called
    assert "tbm=shop" in request_mock.calls[0].request.url.query.decode("utf-8")


@respx.mock
def test_youtube_search_tool() -> None:
    tool = ZenserpYouTubeSearchTool()
    assert tool.name == "zenserp_youtube_search"

    request_mock = respx.get("https://app.zenserp.com/api/v2/search").mock(
        return_value=Response(200, json=MOCK_SEARCH_RESPONSE)
    )

    tool.run({"q": "python tutorial"})
    assert request_mock.called
    assert "search_engine=youtube.com" in request_mock.calls[0].request.url.query.decode("utf-8")


@respx.mock
def test_bing_search_tool() -> None:
    tool = ZenserpBingSearchTool()
    assert tool.name == "zenserp_bing_search"

    request_mock = respx.get("https://app.zenserp.com/api/v2/search").mock(
        return_value=Response(200, json=MOCK_SEARCH_RESPONSE)
    )

    tool.run({"q": "test", "count": 10})
    assert request_mock.called
    assert "search_engine=bing.com" in request_mock.calls[0].request.url.query.decode("utf-8")


@respx.mock
def test_shopping_product_tool() -> None:
    tool = ZenserpShoppingProductTool()
    assert tool.name == "zenserp_shopping_product"

    request_mock = respx.get("https://app.zenserp.com/api/v1/shopping").mock(
        return_value=Response(200, json={"product": {"title": "Test Product"}})
    )

    res = tool.run({"product_id": "12345"})
    assert "Test Product" in res
    assert request_mock.called


@respx.mock
def test_trends_tool() -> None:
    tool = ZenserpTrendsTool()
    assert tool.name == "zenserp_trends"

    request_mock = respx.get("https://app.zenserp.com/api/v1/trends").mock(
        return_value=Response(200, json={"interest_over_time": {}})
    )

    tool.run({"keywords": ["python", "javascript"]})
    assert request_mock.called
    query = request_mock.calls[0].request.url.query.decode("utf-8")
    assert "keyword%5B%5D=python" in query
    assert "keyword%5B%5D=javascript" in query


@respx.mock
def test_trending_tool() -> None:
    tool = ZenserpTrendingTool()
    assert tool.name == "zenserp_trending"

    request_mock = respx.get("https://app.zenserp.com/api/v1/trends/trending").mock(
        return_value=Response(200, json={"trending_searches": []})
    )

    tool.run({})
    assert request_mock.called


@respx.mock
def test_status_tool() -> None:
    tool = ZenserpStatusTool()
    assert tool.name == "zenserp_status"

    request_mock = respx.get("https://app.zenserp.com/api/v2/status").mock(
        return_value=Response(200, json={"remaining_requests": 100})
    )

    res = tool.run({})
    assert "remaining_requests" in res
    assert request_mock.called


@respx.mock
def test_languages_tool() -> None:
    tool = ZenserpLanguagesTool()
    assert tool.name == "zenserp_languages"

    request_mock = respx.get("https://app.zenserp.com/api/v2/hl").mock(
        return_value=Response(200, json={"languages": [{"code": "en", "name": "English"}]})
    )

    res = tool.run({})
    assert "English" in res
    assert request_mock.called


@respx.mock
def test_countries_tool() -> None:
    tool = ZenserpCountriesTool()
    assert tool.name == "zenserp_countries"

    request_mock = respx.get("https://app.zenserp.com/api/v2/gl").mock(
        return_value=Response(200, json={"countries": [{"code": "us", "name": "United States"}]})
    )

    res = tool.run({})
    assert "United States" in res
    assert request_mock.called


@respx.mock
def test_locations_tool() -> None:
    tool = ZenserpLocationsTool()
    assert tool.name == "zenserp_locations"

    request_mock = respx.get("https://app.zenserp.com/api/v2/locations").mock(
        return_value=Response(200, json={"locations": [{"name": "New York"}]})
    )

    res = tool.run({})
    assert "New York" in res
    assert request_mock.called


@respx.mock
def test_search_engines_tool() -> None:
    tool = ZenserpSearchEnginesTool()
    assert tool.name == "zenserp_search_engines"

    request_mock = respx.get("https://app.zenserp.com/api/v2/search_engines").mock(
        return_value=Response(200, json={"search_engines": ["google.com", "bing.com"]})
    )

    res = tool.run({})
    assert "google.com" in res
    assert request_mock.called


def test_toolkit() -> None:
    toolkit = ZenserpToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 18
    names = {t.name for t in tools}
    expected = {
        "zenserp_search",
        "zenserp_image_search",
        "zenserp_video_search",
        "zenserp_news_search",
        "zenserp_shopping_search",
        "zenserp_maps_search",
        "zenserp_reverse_image_search",
        "zenserp_youtube_search",
        "zenserp_bing_search",
        "zenserp_yandex_search",
        "zenserp_shopping_product",
        "zenserp_trends",
        "zenserp_trending",
        "zenserp_status",
        "zenserp_languages",
        "zenserp_countries",
        "zenserp_locations",
        "zenserp_search_engines",
    }
    assert names == expected


def test_simulation_engine() -> None:
    engine = ZenserpSimulationEngine()
    engine.register(
        tool_name="zenserp_search",
        input_match={"q": "test"},
        output='{"mocked": true}',
    )
    res = engine.run("zenserp_search", {"q": "test"})
    assert res == '{"mocked": true}'
    assert engine.call_count == 1
