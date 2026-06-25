"""
Pydantic input models for the Numverify service tools.
"""

from pydantic import BaseModel, Field


class NumverifyValidateInput(BaseModel):
    """Input schema for phone number validation."""

    number: str = Field(
        description="Phone number to validate (international format like '+14158586273' or national format)."
    )
    country_code: str | None = Field(
        default=None,
        description="Two-letter ISO country code. Required when using national format numbers.",
    )


class NumverifyCountriesInput(BaseModel):
    """Input schema for listing supported countries."""
