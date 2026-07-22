from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from pymcpx.services.zenserp.SimulationEngine.models import (
    ZenserpEmptyInput,
    ZenserpSearchInput,
    ZenserpShoppingInput,
    ZenserpTrendingInput,
    ZenserpTrendsInput,
)
from pymcpx.services.zenserp.SimulationEngine.utils import (
    get_countries,
    get_languages,
    get_locations,
    get_search_engines,
    get_shopping_product,
    get_status,
    get_trending,
    get_trends,
    search,
)


class ZenserpSearchTool(BaseTool):
    """Google SERP search via Zenserp."""

    name: str = "zenserp_search"
    description: str = (
        "Search Google for web results. Supports location targeting, pagination, "
        "device type (desktop/mobile/tablet), time filtering, country/language codes, "
        "and more. Use for general web searches. For images use zenserp_image_search, "
        "for videos use zenserp_video_search, for maps use zenserp_maps_search, "
        "for shopping use zenserp_shopping_search, for news use zenserp_news_search."
    )
    args_schema: type[BaseModel] = ZenserpSearchInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return search(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpImageSearchTool(BaseTool):
    """Google Image search via Zenserp."""

    name: str = "zenserp_image_search"
    description: str = (
        "Search Google Images. Supports the same parameters as zenserp_search "
        "but automatically sets the image search type. Use for finding images by keyword."
    )
    args_schema: type[BaseModel] = ZenserpSearchInput

    def _run(self, **kwargs: Any) -> str:
        try:
            kwargs.pop("tbm", None)
            return search(**kwargs, tbm="isch")
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpVideoSearchTool(BaseTool):
    """Google Video search via Zenserp."""

    name: str = "zenserp_video_search"
    description: str = (
        "Search Google Videos. Supports the same parameters as zenserp_search "
        "but automatically sets the video search type."
    )
    args_schema: type[BaseModel] = ZenserpSearchInput

    def _run(self, **kwargs: Any) -> str:
        try:
            kwargs.pop("tbm", None)
            return search(**kwargs, tbm="vid")
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpNewsSearchTool(BaseTool):
    """Google News search via Zenserp."""

    name: str = "zenserp_news_search"
    description: str = (
        "Search Google News. Supports the same parameters as zenserp_search "
        "but automatically sets the news search type."
    )
    args_schema: type[BaseModel] = ZenserpSearchInput

    def _run(self, **kwargs: Any) -> str:
        try:
            kwargs.pop("tbm", None)
            return search(**kwargs, tbm="nws")
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpShoppingSearchTool(BaseTool):
    """Google Shopping search via Zenserp."""

    name: str = "zenserp_shopping_search"
    description: str = (
        "Search Google Shopping for products. Supports the same parameters as "
        "zenserp_search but automatically sets the shopping search type."
    )
    args_schema: type[BaseModel] = ZenserpSearchInput

    def _run(self, **kwargs: Any) -> str:
        try:
            kwargs.pop("tbm", None)
            return search(**kwargs, tbm="shop")
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpMapsSearchTool(BaseTool):
    """Google Maps / Local search via Zenserp."""

    name: str = "zenserp_maps_search"
    description: str = (
        "Search Google Maps / local results. Supports the same parameters as "
        "zenserp_search but automatically sets the maps search type. "
        "Use ll (latitude,longitude) for location-based results."
    )
    args_schema: type[BaseModel] = ZenserpSearchInput

    def _run(self, **kwargs: Any) -> str:
        try:
            kwargs.pop("tbm", None)
            return search(**kwargs, tbm="lcl")
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpImageReverseSearchTool(BaseTool):
    """Google Reverse Image Search via Zenserp."""

    name: str = "zenserp_reverse_image_search"
    description: str = (
        "Search by image URL (reverse image search). Requires image_url parameter "
        "with the URL of the image to search for. Supports all other search parameters."
    )
    args_schema: type[BaseModel] = ZenserpSearchInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return search(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpYouTubeSearchTool(BaseTool):
    """YouTube search via Zenserp."""

    name: str = "zenserp_youtube_search"
    description: str = (
        "Search YouTube videos via Zenserp. Supports the same parameters as "
        "zenserp_search but automatically targets youtube.com. "
        "Use sp for YouTube-specific search parameters."
    )
    args_schema: type[BaseModel] = ZenserpSearchInput

    def _run(self, **kwargs: Any) -> str:
        try:
            kwargs.pop("search_engine", None)
            return search(**kwargs, search_engine="youtube.com")
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpBingSearchTool(BaseTool):
    """Bing search via Zenserp."""

    name: str = "zenserp_bing_search"
    description: str = (
        "Search Bing via Zenserp. Supports the same parameters as zenserp_search "
        "but automatically targets bing.com. Use first/count for pagination, "
        "cc/mkt for country/market, lat/lon for location."
    )
    args_schema: type[BaseModel] = ZenserpSearchInput

    def _run(self, **kwargs: Any) -> str:
        try:
            kwargs.pop("search_engine", None)
            return search(**kwargs, search_engine="bing.com")
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpYandexSearchTool(BaseTool):
    """Yandex search via Zenserp."""

    name: str = "zenserp_yandex_search"
    description: str = (
        "Search Yandex via Zenserp. Supports the same parameters as zenserp_search "
        "but automatically targets yandex.com. Use p for page number, numdoc for results per page, "
        "lang for language, cc for country."
    )
    args_schema: type[BaseModel] = ZenserpSearchInput

    def _run(self, **kwargs: Any) -> str:
        try:
            kwargs.pop("search_engine", None)
            return search(**kwargs, search_engine="yandex.com")
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpShoppingProductTool(BaseTool):
    """Shopping product page details."""

    name: str = "zenserp_shopping_product"
    description: str = (
        "Retrieve detailed information about a specific shopping product page. "
        "Requires the product_id from a shopping search result."
    )
    args_schema: type[BaseModel] = ZenserpShoppingInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_shopping_product(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpTrendsTool(BaseTool):
    """Google Trends data."""

    name: str = "zenserp_trends"
    description: str = (
        "Retrieve Google Trends data for one or more keywords (up to 5). "
        "Returns interest over time, related queries, and regional interest. "
        "Supports category, timeframe, language, and geography filtering."
    )
    args_schema: type[BaseModel] = ZenserpTrendsInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_trends(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpTrendingTool(BaseTool):
    """Google Trending searches."""

    name: str = "zenserp_trending"
    description: str = (
        "Retrieve Google Trending searches (what's trending on Google). "
        "Optionally filter by category (all, business, entertainment, health, science, tech), "
        "language, and geography."
    )
    args_schema: type[BaseModel] = ZenserpTrendingInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_trending(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpStatusTool(BaseTool):
    """Zenserp account status."""

    name: str = "zenserp_status"
    description: str = (
        "Check your Zenserp account status, including remaining API requests "
        "and plan information."
    )
    args_schema: type[BaseModel] = ZenserpEmptyInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_status(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpLanguagesTool(BaseTool):
    """List supported Google interface languages."""

    name: str = "zenserp_languages"
    description: str = "List all supported Google interface language codes (hl values)."
    args_schema: type[BaseModel] = ZenserpEmptyInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_languages(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpCountriesTool(BaseTool):
    """List supported Google country codes."""

    name: str = "zenserp_countries"
    description: str = "List all supported Google country codes (gl values)."
    args_schema: type[BaseModel] = ZenserpEmptyInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_countries(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpLocationsTool(BaseTool):
    """List supported geo locations."""

    name: str = "zenserp_locations"
    description: str = "List all supported geo locations for location-based searches."
    args_schema: type[BaseModel] = ZenserpEmptyInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_locations(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpSearchEnginesTool(BaseTool):
    """List available search engines."""

    name: str = "zenserp_search_engines"
    description: str = "List all available search engines supported by Zenserp."
    args_schema: type[BaseModel] = ZenserpEmptyInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return get_search_engines(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ZenserpToolkit:
    """Convenience bundle that exposes all Zenserp tools."""

    def get_tools(self) -> list[BaseTool]:
        return [
            ZenserpSearchTool(),
            ZenserpImageSearchTool(),
            ZenserpVideoSearchTool(),
            ZenserpNewsSearchTool(),
            ZenserpShoppingSearchTool(),
            ZenserpMapsSearchTool(),
            ZenserpImageReverseSearchTool(),
            ZenserpYouTubeSearchTool(),
            ZenserpBingSearchTool(),
            ZenserpYandexSearchTool(),
            ZenserpShoppingProductTool(),
            ZenserpTrendsTool(),
            ZenserpTrendingTool(),
            ZenserpStatusTool(),
            ZenserpLanguagesTool(),
            ZenserpCountriesTool(),
            ZenserpLocationsTool(),
            ZenserpSearchEnginesTool(),
        ]


MCP_TOOLS: list[BaseTool] = [
    ZenserpSearchTool(),
    ZenserpImageSearchTool(),
    ZenserpVideoSearchTool(),
    ZenserpNewsSearchTool(),
    ZenserpShoppingSearchTool(),
    ZenserpMapsSearchTool(),
    ZenserpImageReverseSearchTool(),
    ZenserpYouTubeSearchTool(),
    ZenserpBingSearchTool(),
    ZenserpYandexSearchTool(),
    ZenserpShoppingProductTool(),
    ZenserpTrendsTool(),
    ZenserpTrendingTool(),
    ZenserpStatusTool(),
    ZenserpLanguagesTool(),
    ZenserpCountriesTool(),
    ZenserpLocationsTool(),
    ZenserpSearchEnginesTool(),
]
