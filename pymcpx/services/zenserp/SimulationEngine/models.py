from pydantic import BaseModel, Field


class ZenserpSearchInput(BaseModel):
    """Input schema for Zenserp search (Google, Bing, Yandex, YouTube)."""

    q: str = Field(..., description="Search query string.")
    location: str | None = Field(
        default=None,
        description="Location for localized results (e.g. 'Austin, Texas, United States').",
    )
    search_engine: str | None = Field(
        default=None,
        description="Search engine: 'google.com' (default), 'bing.com', 'yandex.com', 'youtube.com'.",
    )
    start: int | None = Field(default=None, description="Result offset for pagination (Google, default 0).")
    num: int | None = Field(default=None, description="Number of results per page (Google, default 10).")
    tbm: str | None = Field(
        default=None,
        description="Search type: 'isch' (images), 'vid' (videos), 'lcl'/'map' (maps), 'shop' (shopping), 'nws' (news).",
    )
    device: str | None = Field(
        default=None, description="Device type: 'desktop', 'mobile', 'tablet'."
    )
    timeframe: str | None = Field(
        default=None,
        description="Time range: 'd' (past 24h), 'w' (past week), 'm' (past month), 'y' (past year).",
    )
    gl: str | None = Field(default=None, description="Google country code (e.g. 'us', 'de', 'fr').")
    hl: str | None = Field(default=None, description="Google interface language (e.g. 'en', 'de', 'fr').")
    lr: str | None = Field(default=None, description="Language restriction (e.g. 'lang_en').")
    output: str | None = Field(default=None, description="Output format: 'json' (default) or 'html'.")
    image_url: str | None = Field(default=None, description="URL for reverse image search.")
    ll: str | None = Field(default=None, description="Latitude,longitude for map search (e.g. '40.7128,-74.0060').")
    sp: str | None = Field(default=None, description="YouTube search parameter.")
    cc: str | None = Field(default=None, description="Country code for Bing/Yandex.")
    mkt: str | None = Field(default=None, description="Market code for Bing (e.g. 'en-US').")
    lat: str | None = Field(default=None, description="Latitude for Bing/Yandex.")
    lon: str | None = Field(default=None, description="Longitude for Bing/Yandex.")
    first: int | None = Field(default=None, description="First result position for Bing (default 1).")
    count: int | None = Field(default=None, description="Number of results for Bing (default 10).")
    p: int | None = Field(default=None, description="Page number for Yandex (default 1).")
    numdoc: int | None = Field(default=None, description="Number of results for Yandex (default 10).")
    lang: str | None = Field(default=None, description="Search language for Yandex (e.g. 'en', 'ru').")
    within: str | None = Field(default=None, description="Site restriction (e.g. 'site:example.com').")
    uule: str | None = Field(default=None, description="Encoded UULE parameter for Google location targeting.")


class ZenserpShoppingInput(BaseModel):
    """Input schema for Zenserp shopping product page."""

    product_id: str = Field(..., description="Shopping product ID to retrieve details for.")
    location: str | None = Field(default=None, description="Location for localized results.")
    search_engine: str | None = Field(
        default=None, description="Search engine (default 'google.com')."
    )
    hl: str | None = Field(default=None, description="Interface language.")
    gl: str | None = Field(default=None, description="Country code.")


class ZenserpTrendsInput(BaseModel):
    """Input schema for Google Trends."""

    keywords: list[str] = Field(
        ..., description="Keywords for trend comparison (up to 5, passed as keyword[] params)."
    )
    cat: str | None = Field(default=None, description="Google Trends category ID.")
    timeframe: str | None = Field(
        default=None,
        description="Timeframe: 'today 12-m', 'today 3-m', 'today 1-m', 'today 7-d', 'today 1-d', 'now 1-H', 'now 4-H', 'all'.",
    )
    type: str | None = Field(
        default=None, description="Trend type: 'default' or 'related_queries'."
    )
    hl: str | None = Field(default=None, description="Interface language.")
    geo: str | None = Field(default=None, description="Geographic location (e.g. 'US', 'US-CA').")


class ZenserpTrendingInput(BaseModel):
    """Input schema for Google Trending searches."""

    cat: str | None = Field(
        default=None,
        description="Category: 'all', 'b' (business), 'e' (entertainment), 'm' (health), 's' (science), 't' (tech).",
    )
    hl: str | None = Field(default=None, description="Interface language.")
    geo: str | None = Field(default=None, description="Geographic location.")


class ZenserpEmptyInput(BaseModel):
    """Input schema for list endpoints with no required parameters."""
