from pydantic import BaseModel, Field


class ExchangeratehostLiveInput(BaseModel):
    """Input schema for real-time exchange rates."""

    source: str | None = Field(
        default=None,
        description="Source/base currency (3-letter code, default USD).",
        pattern="^[A-Z]{3}$",
    )
    currencies: str | None = Field(
        default=None,
        description="Comma-separated list of currencies to limit results (e.g. 'USD,GBP,EUR').",
    )


class ExchangeratehostHistoricalInput(BaseModel):
    """Input schema for historical exchange rates."""

    date: str = Field(..., description="Historical date in YYYY-MM-DD format.")
    source: str | None = Field(
        default=None,
        description="Source/base currency (3-letter code, default USD).",
        pattern="^[A-Z]{3}$",
    )
    currencies: str | None = Field(
        default=None,
        description="Comma-separated list of currencies to limit results (e.g. 'USD,GBP,EUR').",
    )


class ExchangeratehostConvertInput(BaseModel):
    """Input schema for currency conversion."""

    from_: str = Field(
        ..., description="Source currency code (3-letter ISO or crypto) to convert from."
    )
    to: str = Field(..., description="Target currency code (3-letter ISO or crypto) to convert to.")
    amount: float = Field(..., description="Amount to convert.", gt=0)
    date: str | None = Field(
        default=None, description="Historical date in YYYY-MM-DD format for conversion."
    )


class ExchangeratehostTimeframeInput(BaseModel):
    """Input schema for time-series exchange rates."""

    start_date: str = Field(..., description="Start date in YYYY-MM-DD format (max 365 day window).")
    end_date: str = Field(..., description="End date in YYYY-MM-DD format.")
    source: str | None = Field(
        default=None,
        description="Source/base currency (3-letter code, default USD).",
        pattern="^[A-Z]{3}$",
    )
    currencies: str | None = Field(
        default=None,
        description="Comma-separated list of currencies to limit results (e.g. 'USD,GBP,EUR').",
    )


class ExchangeratehostChangeInput(BaseModel):
    """Input schema for currency change/fluctuation."""

    start_date: str = Field(..., description="Start date in YYYY-MM-DD format (max 365 day window).")
    end_date: str = Field(..., description="End date in YYYY-MM-DD format.")
    source: str | None = Field(
        default=None,
        description="Source/base currency (3-letter code, default USD).",
        pattern="^[A-Z]{3}$",
    )
    currencies: str | None = Field(
        default=None,
        description="Comma-separated list of currencies to limit results (e.g. 'USD,GBP,EUR').",
    )
