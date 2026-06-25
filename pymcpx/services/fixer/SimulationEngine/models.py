"""
Pydantic input models for the Fixer service tools.
"""

from pydantic import BaseModel, Field


class FixerSymbolsInput(BaseModel):
    """Input schema for listing supported currency symbols."""


class FixerLatestRatesInput(BaseModel):
    """Input schema for latest exchange rates lookup."""

    base: str = Field(
        default="EUR",
        description="Base currency (three-letter ISO code, e.g. 'USD'). Defaults to EUR.",
    )
    symbols: str | None = Field(
        default=None,
        description="Comma-separated currency codes to filter rates (e.g., 'USD,GBP,JPY').",
    )


class FixerHistoricalRatesInput(BaseModel):
    """Input schema for historical exchange rates lookup."""

    date: str = Field(
        description="Historical date (Format: 'YYYY-MM-DD'). Rates available back to 1999."
    )
    base: str = Field(
        default="EUR",
        description="Base currency (three-letter ISO code). Defaults to EUR.",
    )
    symbols: str | None = Field(
        default=None,
        description="Comma-separated currency codes to filter rates.",
    )


class FixerConvertInput(BaseModel):
    """Input schema for currency conversion."""

    from_: str = Field(
        description="Source currency code (e.g., 'GBP').",
    )
    to: str = Field(
        description="Target currency code (e.g., 'JPY').",
    )
    amount: float = Field(
        description="Amount to convert (positive number).",
    )
    date: str | None = Field(
        default=None,
        description="Optional historical date (Format: 'YYYY-MM-DD') for conversion at past rates.",
    )


class FixerTimeSeriesInput(BaseModel):
    """Input schema for time-series rates lookup."""

    start_date: str = Field(
        description="Start date inclusive (Format: 'YYYY-MM-DD'). Max 365 day window."
    )
    end_date: str = Field(description="End date inclusive (Format: 'YYYY-MM-DD').")
    base: str = Field(
        default="EUR",
        description="Base currency (three-letter ISO code). Defaults to EUR.",
    )
    symbols: str | None = Field(
        default=None,
        description="Comma-separated currency codes to filter rates.",
    )


class FixerFluctuationInput(BaseModel):
    """Input schema for currency fluctuation analysis."""

    start_date: str = Field(
        description="Start date inclusive (Format: 'YYYY-MM-DD'). Max 365 day window."
    )
    end_date: str = Field(description="End date inclusive (Format: 'YYYY-MM-DD').")
    base: str = Field(
        default="EUR",
        description="Base currency (three-letter ISO code). Defaults to EUR.",
    )
    symbols: str | None = Field(
        default=None,
        description="Comma-separated currency codes to filter rates.",
    )
