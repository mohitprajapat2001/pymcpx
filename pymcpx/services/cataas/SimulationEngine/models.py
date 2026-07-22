"""
Pydantic input/output models for the cataas service tools.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class _CatImageMixin(BaseModel):
    """Flattened image transformation parameters shared across cat endpoints."""

    model_config = {"populate_by_name": True}

    type: str | None = Field(
        default=None,
        description="Image type: square, medium, small, xsmall.",
    )
    filter: str | None = Field(
        default=None,
        description="Filter: mono, negate, custom.",
    )
    fit: str | None = Field(
        default=None,
        description="Fit: cover, contain, fill, inside, outside.",
    )
    position: str | None = Field(
        default=None,
        description="Position: top, right top, right, right bottom, bottom, left bottom, left, left top, center.",
    )
    width: int | None = Field(default=None, ge=1, description="Width in pixels.")
    height: int | None = Field(default=None, ge=1, description="Height in pixels.")
    blur: int | None = Field(default=None, ge=0, description="Blur radius.")
    r: int | None = Field(
        default=None, ge=0, le=255, description="Red value 0-255 (custom filter)."
    )
    g: int | None = Field(
        default=None, ge=0, le=255, description="Green value 0-255 (custom filter)."
    )
    b: int | None = Field(
        default=None, ge=0, le=255, description="Blue value 0-255 (custom filter)."
    )
    brightness: int | None = Field(default=None, description="Brightness (custom filter).")
    saturation: int | None = Field(default=None, description="Saturation (custom filter).")
    hue: int | None = Field(default=None, description="Hue (custom filter).")
    lightness: int | None = Field(default=None, description="Lightness (custom filter).")
    html: bool | None = Field(default=None, description="Return HTML.")
    return_json: bool | None = Field(
        default=None, alias="json", description="Return JSON metadata instead of image."
    )


class _CatTextMixin(BaseModel):
    """Flattened text overlay parameters for cat saying endpoints."""

    model_config = {"populate_by_name": True}

    font: str | None = Field(
        default=None,
        description="Font name (e.g. Impact, Arial, Comic Sans MS).",
    )
    font_size: int | None = Field(default=None, ge=1, description="Font size.", alias="fontSize")
    font_color: str | None = Field(
        default=None, description="Font color hex (e.g. #fff).", alias="fontColor"
    )
    font_background: str | None = Field(
        default=None,
        description="Font background color (e.g. #000).",
        alias="fontBackground",
    )


class ListTagsInput(BaseModel):
    """Input schema for list_tags tool."""

    search: str | None = Field(
        default=None,
        description="Fuzzy search term to match against available tags.",
    )
    limit: int = Field(
        default=20,
        ge=1,
        le=100,
        description="Maximum number of tags to return.",
    )


class ListCatsInput(BaseModel):
    """Input schema for list_cats tool."""

    limit: int = Field(default=10, ge=1, le=100, description="Maximum number of cats to return.")
    skip: int = Field(default=0, ge=0, description="Number of cats to skip.")
    tags: str | None = Field(
        default=None,
        description="Comma-separated tags to filter cats by.",
    )
    search: str | None = Field(
        default=None,
        description="Fuzzy search term to find matching tags, then filter cats by those tags.",
    )


class CountCatsInput(BaseModel):
    """Input schema for count_cats tool."""


class GetRandomCatInput(_CatImageMixin):
    """Input schema for get_random_cat tool."""


class GetCatByIdInput(_CatImageMixin):
    """Input schema for get_cat_by_id tool."""

    id: str = Field(description="Cat ID to retrieve.")


class GetCatByTagInput(_CatImageMixin):
    """Input schema for get_cat_by_tag tool."""

    tag: str = Field(description="Tag to filter cat by.")


class GetRandomCatSayingInput(_CatImageMixin, _CatTextMixin):
    """Input schema for get_random_cat_saying tool."""

    text: str = Field(description="Text for the cat to say.")


class GetCatByIdSayingInput(_CatImageMixin, _CatTextMixin):
    """Input schema for get_cat_by_id_saying tool."""

    id: str = Field(description="Cat ID.")
    text: str = Field(description="Text for the cat to say.")


class GetRandomCatByTagSayingInput(_CatImageMixin, _CatTextMixin):
    """Input schema for get_random_cat_by_tag_saying tool."""

    tag: str = Field(description="Tag to filter cat by.")
    text: str = Field(description="Text for the cat to say.")


class CatModel(BaseModel):
    """Output model for a cat from the CATAAS API."""

    id: str = Field(description="Cat ID.")
    tags: list[str] = Field(description="Tags associated with the cat.")
    mimetype: str = Field(description="MIME type of the cat image.")
    created_at: str = Field(description="Creation date.", alias="createdAt")


class CatCountModel(BaseModel):
    """Output model for cat count."""

    count: int = Field(description="Number of cats.")
