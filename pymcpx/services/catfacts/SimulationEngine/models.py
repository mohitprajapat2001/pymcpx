"""
Pydantic input models for the catfacts service tools.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class GetBreedsInput(BaseModel):
    """Input schema for get_breeds tool."""

    limit: int | None = Field(
        default=None,
        description="Limit the number of breeds returned.",
        ge=1,
    )


class GetRandomFactInput(BaseModel):
    """Input schema for get_random_fact tool."""

    max_length: int | None = Field(
        default=None,
        description="Maximum length of the returned fact.",
        ge=1,
    )


class GetFactsInput(BaseModel):
    """Input schema for get_facts tool."""

    max_length: int | None = Field(
        default=None,
        description="Maximum length of each returned fact.",
        ge=1,
    )
    limit: int | None = Field(
        default=None,
        description="Limit the number of facts returned.",
        ge=1,
    )


class BreedModel(BaseModel):
    """Output model for a cat breed."""

    breed: str = Field(description="Breed name.")
    country: str = Field(description="Country of origin.")
    origin: str = Field(description="Geographic origin.")
    coat: str = Field(description="Coat type.")
    pattern: str = Field(description="Pattern type.")


class CatFactModel(BaseModel):
    """Output model for a cat fact."""

    fact: str = Field(description="The cat fact.")
    length: int = Field(description="Length of the fact in characters.")
