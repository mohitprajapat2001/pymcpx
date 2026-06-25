# Aviationstack Service

MCP-compatible LangChain tools for the [Aviationstack API](https://aviationstack.com/) — real-time and historical flight tracking, airport/airline information, schedules, and more.

## Prerequisites

- An Aviationstack API access key (free tier available at [aviationstack.com](https://aviationstack.com/))
- Python 3.11+

## Installation

```bash
pip install pymcpx[aviationstack]
```

Set your API key as an environment variable:

```bash
export AVIATIONSTACK_ACCESS_KEY="your_api_key_here"
```

## Tools

| Tool Name                           | Class                              | Description                                                              | Input Keys                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------- | ---------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aviationstack_flights`             | `AviationstackFlightsTool`         | Real-time and historical flight tracking worldwide                       | `limit`, `offset`, `flight_date`, `flight_status`, `dep_iata`, `arr_iata`, `dep_icao`, `arr_icao`, `airline_name`, `airline_iata`, `airline_icao`, `flight_number`, `flight_iata`, `flight_icao`, `min_delay_dep`, `max_delay_dep`, `min_delay_arr`, `max_delay_arr`, `arr_scheduled_time_arr`, `dep_scheduled_time_dep`                                                                                                                                                            |
| `aviationstack_routes`              | `AviationstackRoutesTool`          | Airline route information                                               | `limit`, `offset`, `dep_iata`, `arr_iata`, `dep_icao`, `arr_icao`, `airline_iata`, `airline_icao`, `flight_number`                                                                                                                                                                                                                                                                                                                                                                  |
| `aviationstack_airports`            | `AviationstackAirportsTool`        | Airport information including IATA/ICAO codes, timezone, coordinates     | `limit`, `offset`, `search`                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `aviationstack_airlines`            | `AviationstackAirlinesTool`        | Airline information including IATA/ICAO codes and country                | `limit`, `offset`, `search`                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `aviationstack_airplanes`           | `AviationstackAirplanesTool`       | Airplane/aircraft registration and model information                     | `limit`, `offset`, `search`                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `aviationstack_aircraft_types`      | `AviationstackAircraftTypesTool`   | Aircraft type codes and descriptions                                    | `limit`, `offset`, `search`                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `aviationstack_taxes`               | `AviationstackTaxesTool`           | Aviation tax codes and amounts                                          | `limit`, `offset`, `search`                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `aviationstack_cities`              | `AviationstackCitiesTool`          | City information including IATA code and timezone                        | `limit`, `offset`, `search`                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `aviationstack_countries`           | `AviationstackCountriesTool`       | Country information including ISO codes                                  | `limit`, `offset`, `search`                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `aviationstack_timetable`           | `AviationstackTimetableTool`       | Real-time flight schedules (arrivals/departures) for an airport          | `iata_code`, `type`, `status`, `dep_terminal`, `dep_delay`, `dep_sch_time`, `dep_est_time`, `dep_act_time`, `dep_est_runway`, `dep_act_runway`, `arr_terminal`, `arr_delay`, `arr_sch_time`, `arr_est_time`, `arr_act_time`, `arr_est_runway`, `arr_act_runway`, `airline_name`, `airline_iata`, `airline_icao`, `flight_number`, `flight_iata`, `flight_icao`, `limit`, `offset`                                                                                                   |
| `aviationstack_flights_future`      | `AviationstackFlightsFutureTool`   | Future flight schedules for an airport                                   | `iata_code`, `type`, `date`, `airline_iata`, `airline_icao`, `flight_number`, `limit`, `offset`                                                                                                                                                                                                                                                                                                                                                                                    |

## Usage Examples

### Individual Tool

```python
import os
os.environ["AVIATIONSTACK_ACCESS_KEY"] = "your_key"

from pymcpx.aviationstack import AviationstackFlightsTool

tool = AviationstackFlightsTool()
result = tool.run({
    "flight_date": "2025-09-15",
    "dep_iata": "JFK",
    "arr_iata": "LAX",
})
print(result)
```

### Toolkit (all tools)

```python
import os
os.environ["AVIATIONSTACK_ACCESS_KEY"] = "your_key"

from pymcpx.aviationstack import AviationstackToolkit

toolkit = AviationstackToolkit()
tools = toolkit.get_tools()
results = tools[0].run({"dep_iata": "JFK"})
print(results)
```

### MCP Integration

```python
from pymcpx.aviationstack import MCP_TOOLS

# Pass MCP_TOOLS to your MCP-compatible agent framework
# Each tool exposes a stable name and JSON schema
for tool in MCP_TOOLS:
    print(f"{tool.name}: {tool.description}")
```
