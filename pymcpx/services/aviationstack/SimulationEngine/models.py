from pydantic import BaseModel, Field


class AviationstackFlightsInput(BaseModel):
    """Input schema for real-time and historical flight tracking."""

    limit: int | None = Field(default=None, description="Number of results to return (max 1000).")
    offset: int | None = Field(default=None, description="Offset for pagination.")
    flight_date: str | None = Field(
        default=None,
        description="Flight date (Format: 'YYYY-MM-DD'). Historical data available for last 3 months.",
    )
    flight_status: str | None = Field(
        default=None,
        description="Filter by flight status: 'scheduled', 'active', 'landed', 'cancelled', 'incident', 'diverted'.",
    )
    dep_iata: str | None = Field(
        default=None, description="Departure airport IATA code (e.g. 'JFK')."
    )
    arr_iata: str | None = Field(
        default=None, description="Arrival airport IATA code (e.g. 'LAX')."
    )
    dep_icao: str | None = Field(default=None, description="Departure airport ICAO code.")
    arr_icao: str | None = Field(default=None, description="Arrival airport ICAO code.")
    airline_name: str | None = Field(
        default=None, description="Airline name (e.g. 'American Airlines')."
    )
    airline_iata: str | None = Field(default=None, description="Airline IATA code (e.g. 'AA').")
    airline_icao: str | None = Field(default=None, description="Airline ICAO code.")
    flight_number: str | None = Field(default=None, description="Flight number (e.g. '100').")
    flight_iata: str | None = Field(default=None, description="Flight IATA code (e.g. 'AA100').")
    flight_icao: str | None = Field(default=None, description="Flight ICAO code.")
    min_delay_dep: int | None = Field(
        default=None, description="Minimum departure delay in minutes."
    )
    max_delay_dep: int | None = Field(
        default=None, description="Maximum departure delay in minutes."
    )
    min_delay_arr: int | None = Field(default=None, description="Minimum arrival delay in minutes.")
    max_delay_arr: int | None = Field(default=None, description="Maximum arrival delay in minutes.")
    arr_scheduled_time_arr: str | None = Field(
        default=None,
        description="Arrival scheduled time from (Format: 'YYYY-MM-DD HH:MM:SS').",
    )
    dep_scheduled_time_dep: str | None = Field(
        default=None,
        description="Departure scheduled time from (Format: 'YYYY-MM-DD HH:MM:SS').",
    )


class AviationstackRoutesInput(BaseModel):
    """Input schema for airline route lookup."""

    limit: int | None = Field(default=None, description="Number of results to return.")
    offset: int | None = Field(default=None, description="Offset for pagination.")
    dep_iata: str | None = Field(default=None, description="Departure airport IATA code.")
    arr_iata: str | None = Field(default=None, description="Arrival airport IATA code.")
    dep_icao: str | None = Field(default=None, description="Departure airport ICAO code.")
    arr_icao: str | None = Field(default=None, description="Arrival airport ICAO code.")
    airline_iata: str | None = Field(default=None, description="Airline IATA code.")
    airline_icao: str | None = Field(default=None, description="Airline ICAO code.")
    flight_number: str | None = Field(default=None, description="Flight number.")


class AviationstackAirportsInput(BaseModel):
    """Input schema for airport information."""

    limit: int | None = Field(default=None, description="Number of results to return.")
    offset: int | None = Field(default=None, description="Offset for pagination.")
    search: str | None = Field(
        default=None,
        description="Search term for airport name, IATA code, ICAO code, or city.",
    )


class AviationstackAirlinesInput(BaseModel):
    """Input schema for airline information."""

    limit: int | None = Field(default=None, description="Number of results to return.")
    offset: int | None = Field(default=None, description="Offset for pagination.")
    search: str | None = Field(
        default=None, description="Search term for airline name, IATA code, or ICAO code."
    )


class AviationstackAirplanesInput(BaseModel):
    """Input schema for airplane/aircraft information."""

    limit: int | None = Field(default=None, description="Number of results to return.")
    offset: int | None = Field(default=None, description="Offset for pagination.")
    search: str | None = Field(
        default=None, description="Search term for airplane name or ICAO code."
    )


class AviationstackAircraftTypesInput(BaseModel):
    """Input schema for aircraft type codes."""

    limit: int | None = Field(default=None, description="Number of results to return.")
    offset: int | None = Field(default=None, description="Offset for pagination.")
    search: str | None = Field(
        default=None, description="Search term for aircraft type name or code."
    )


class AviationstackTaxesInput(BaseModel):
    """Input schema for aviation tax information."""

    limit: int | None = Field(default=None, description="Number of results to return.")
    offset: int | None = Field(default=None, description="Offset for pagination.")
    search: str | None = Field(default=None, description="Search term for tax description or code.")


class AviationstackCitiesInput(BaseModel):
    """Input schema for city information."""

    limit: int | None = Field(default=None, description="Number of results to return.")
    offset: int | None = Field(default=None, description="Offset for pagination.")
    search: str | None = Field(
        default=None, description="Search term for city name, IATA code, or country."
    )


class AviationstackCountriesInput(BaseModel):
    """Input schema for country information."""

    limit: int | None = Field(default=None, description="Number of results to return.")
    offset: int | None = Field(default=None, description="Offset for pagination.")
    search: str | None = Field(default=None, description="Search term for country name or code.")


class AviationstackTimetableInput(BaseModel):
    """Input schema for real-time flight schedules."""

    iata_code: str = Field(description="Airport IATA code to retrieve schedules for.")
    type: str = Field(description="Schedule type: 'arrival' or 'departure'.")
    status: str | None = Field(default=None, description="Flight status filter.")
    dep_terminal: str | None = Field(default=None, description="Departure terminal filter.")
    dep_delay: int | None = Field(default=None, description="Departure delay in minutes.")
    dep_sch_time: str | None = Field(
        default=None, description="Departure scheduled time from (Format: 'YYYY-MM-DD HH:MM:SS')."
    )
    dep_est_time: str | None = Field(
        default=None, description="Departure estimated time from (Format: 'YYYY-MM-DD HH:MM:SS')."
    )
    dep_act_time: str | None = Field(
        default=None, description="Departure actual time from (Format: 'YYYY-MM-DD HH:MM:SS')."
    )
    dep_est_runway: str | None = Field(
        default=None,
        description="Departure estimated runway time from (Format: 'YYYY-MM-DD HH:MM:SS').",
    )
    dep_act_runway: str | None = Field(
        default=None,
        description="Departure actual runway time from (Format: 'YYYY-MM-DD HH:MM:SS').",
    )
    arr_terminal: str | None = Field(default=None, description="Arrival terminal filter.")
    arr_delay: int | None = Field(default=None, description="Arrival delay in minutes.")
    arr_sch_time: str | None = Field(
        default=None, description="Arrival scheduled time from (Format: 'YYYY-MM-DD HH:MM:SS')."
    )
    arr_est_time: str | None = Field(
        default=None, description="Arrival estimated time from (Format: 'YYYY-MM-DD HH:MM:SS')."
    )
    arr_act_time: str | None = Field(
        default=None, description="Arrival actual time from (Format: 'YYYY-MM-DD HH:MM:SS')."
    )
    arr_est_runway: str | None = Field(
        default=None,
        description="Arrival estimated runway time from (Format: 'YYYY-MM-DD HH:MM:SS').",
    )
    arr_act_runway: str | None = Field(
        default=None, description="Arrival actual runway time from (Format: 'YYYY-MM-DD HH:MM:SS')."
    )
    airline_name: str | None = Field(default=None, description="Airline name filter.")
    airline_iata: str | None = Field(default=None, description="Airline IATA code filter.")
    airline_icao: str | None = Field(default=None, description="Airline ICAO code filter.")
    flight_number: str | None = Field(default=None, description="Flight number filter.")
    flight_iata: str | None = Field(default=None, description="Flight IATA code filter.")
    flight_icao: str | None = Field(default=None, description="Flight ICAO code filter.")
    limit: int | None = Field(default=None, description="Number of results to return.")
    offset: int | None = Field(default=None, description="Offset for pagination.")


class AviationstackFutureFlightsInput(BaseModel):
    """Input schema for future flight schedules."""

    iata_code: str = Field(description="Airport IATA code to retrieve future schedules for.")
    type: str = Field(description="Schedule type: 'arrival' or 'departure'.")
    date: str = Field(description="Future date (Format: 'YYYY-MM-DD').")
    airline_iata: str | None = Field(default=None, description="Airline IATA code filter.")
    airline_icao: str | None = Field(default=None, description="Airline ICAO code filter.")
    flight_number: str | None = Field(default=None, description="Flight number filter.")
    limit: int | None = Field(default=None, description="Number of results to return.")
    offset: int | None = Field(default=None, description="Offset for pagination.")
