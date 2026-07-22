"""
Pydantic input/output models for the dogapi service tools.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class ListBreedsInput(BaseModel):
    """Input schema for list_breeds tool."""

    search: str | None = Field(
        default=None,
        description="Fuzzy search term to match against breed names.",
    )
    limit: int = Field(
        default=20,
        ge=1,
        le=100,
        description="Maximum number of breeds to return.",
    )


class GetRandomDogImageInput(BaseModel):
    """Input schema for get_random_dog_image tool."""


class GetRandomDogImageByBreedInput(BaseModel):
    """Input schema for get_random_dog_image_by_breed tool."""

    breed: str = Field(description="Breed name to get a random image for.")
