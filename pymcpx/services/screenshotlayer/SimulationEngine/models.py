from pydantic import BaseModel, Field


class ScreenshotlayerCaptureInput(BaseModel):
    """Input schema for capturing a website screenshot."""

    url: str = Field(..., description="Target URL to capture (must include protocol, e.g. https://).")
    format: str | None = Field(
        default=None,
        description="Output image format: 'PNG' (default), 'JPG'/'JPEG', 'GIF', 'WEBP'.",
    )
    fullpage: int | None = Field(
        default=None,
        description="Set to 1 to capture the full height of the page.",
        ge=0,
        le=1,
    )
    width: int | None = Field(
        default=None,
        description="Thumbnail width in pixels (returns scaled thumbnail preserving aspect ratio).",
        ge=1,
    )
    viewport: str | None = Field(
        default=None,
        description="Viewport size as 'WIDTHxHEIGHT' (e.g. '1440x900'). Default: 1440x900. Max: 5000x5000.",
    )
    css_url: str | None = Field(
        default=None,
        description="URL of a CSS file to inject into the page prior to render (max ~100kB).",
    )
    delay: int | None = Field(
        default=None,
        description="Delay in seconds before capturing (for JS-heavy pages). Max: 20.",
        ge=0,
        le=20,
    )
    ttl: int | None = Field(
        default=None,
        description="Cache TTL in seconds. Default/max: 2592000 (30 days). Min: 300.",
        ge=300,
        le=2592000,
    )
    force: int | None = Field(
        default=None,
        description="Set to 1 to force a fresh capture even if cached.",
        ge=0,
        le=1,
    )
    placeholder: str | None = Field(
        default=None,
        description="Return placeholder image while fresh screenshot is prepared. Use '1' for default or a custom image URL.",
    )
    user_agent: str | None = Field(
        default=None,
        description="Custom User-Agent header for fetching the target page.",
    )
    accept_lang: str | None = Field(
        default=None,
        description="Custom Accept-Language header (e.g. 'en-US,en').",
    )
    export: str | None = Field(
        default=None,
        description="Export to AWS S3 ('s3://key:secret@bucket/path') or FTP ('ftp://user:pass@server/path').",
    )
    secret_key: str | None = Field(
        default=None,
        description="MD5 hash of (target_url + secret_keyword) for URL encryption.",
    )
    scale: float | None = Field(
        default=None,
        description="Device pixel ratio: 1 (default), 1.5, or 2 (Retina).",
    )
    quality: int | None = Field(
        default=None,
        description="Output quality (1-100). Default: 70.",
        ge=1,
        le=100,
    )
