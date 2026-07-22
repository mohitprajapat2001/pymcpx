import os

from httpx import Response
import respx

from pymcpx.services.ebird import (
    EbirdSimulationEngine,
    EbirdToolkit,
    GetHotspotsTool,
    GetNearbyObservationsTool,
    GetRecentObservationsTool,
    GetRecentSpeciesObservationsTool,
    GetSpeciesListTool,
    GetTaxonomyTool,
)

# Mock API token for testing
os.environ["X_EBIRD_API_TOKEN"] = "mock_token"


@respx.mock
def test_get_recent_observations_tool() -> None:
    tool = GetRecentObservationsTool()
    assert tool.name == "get_recent_observations"

    respx.get("https://api.ebird.org/v2/data/obs/US-NY-103/recent?maxResults=5").mock(
        return_value=Response(
            200,
            json=[{"speciesCode": "houfin", "comName": "House Finch", "howMany": 3}],
        )
    )

    res = tool.run({"region_code": "US-NY-103", "max_results": 5})
    assert "House Finch" in res
    assert "houfin" in res


@respx.mock
def test_get_recent_species_observations_tool() -> None:
    tool = GetRecentSpeciesObservationsTool()
    assert tool.name == "get_recent_species_observations"

    respx.get("https://api.ebird.org/v2/data/obs/US-NY-103/recent/houfin?maxResults=5").mock(
        return_value=Response(
            200,
            json=[{"speciesCode": "houfin", "comName": "House Finch", "howMany": 2}],
        )
    )

    res = tool.run({"region_code": "US-NY-103", "species_code": "houfin", "max_results": 5})
    assert "House Finch" in res


@respx.mock
def test_get_nearby_observations_tool() -> None:
    tool = GetNearbyObservationsTool()
    assert tool.name == "get_nearby_observations"

    respx.get(
        "https://api.ebird.org/v2/data/obs/geo/recent/houfin?lat=40.7&lng=-74.0&maxResults=5"
    ).mock(
        return_value=Response(
            200,
            json=[{"speciesCode": "houfin", "comName": "House Finch", "howMany": 1}],
        )
    )

    res = tool.run({"species_code": "houfin", "lat": 40.7, "lng": -74.0, "max_results": 5})
    assert "House Finch" in res


@respx.mock
def test_get_hotspots_tool() -> None:
    tool = GetHotspotsTool()
    assert tool.name == "get_hotspots"

    respx.get("https://api.ebird.org/v2/ref/hotspot/US-NY?maxResults=5").mock(
        return_value=Response(
            200,
            json=[{"locId": "L123", "locName": "Central Park", "lat": 40.78, "lng": -73.97}],
        )
    )

    res = tool.run({"region_code": "US-NY", "max_results": 5})
    assert "Central Park" in res


@respx.mock
def test_get_taxonomy_tool() -> None:
    tool = GetTaxonomyTool()
    assert tool.name == "get_taxonomy"

    respx.get("https://api.ebird.org/v2/ref/taxonomy/ebird").mock(
        return_value=Response(
            200,
            json=[
                {
                    "speciesCode": "houfin",
                    "comName": "House Finch",
                    "sciName": "Haemorhous mexicanus",
                },
                {
                    "speciesCode": "norcar",
                    "comName": "Northern Cardinal",
                    "sciName": "Cardinalis cardinalis",
                },
            ],
        )
    )

    res = tool.run({"search": "finch", "limit": 5})
    assert "House Finch" in res
    assert "Northern Cardinal" not in res


@respx.mock
def test_get_species_list_tool() -> None:
    tool = GetSpeciesListTool()
    assert tool.name == "get_species_list"

    respx.get("https://api.ebird.org/v2/product/spplist/US-NY").mock(
        return_value=Response(
            200,
            json=["houfin", "norcar", "amecro"],
        )
    )

    res = tool.run({"region_code": "US-NY", "search": "finch", "limit": 5})
    assert "houfin" in res


def test_toolkit() -> None:
    toolkit = EbirdToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 6
    names = {t.name for t in tools}
    assert "get_recent_observations" in names
    assert "get_recent_species_observations" in names
    assert "get_nearby_observations" in names
    assert "get_hotspots" in names
    assert "get_taxonomy" in names
    assert "get_species_list" in names


def test_simulation_engine() -> None:
    engine = EbirdSimulationEngine()
    engine.register(
        tool_name="get_taxonomy",
        input_match={"search": "finch"},
        output='[{"comName": "House Finch"}]',
    )
    res = engine.run("get_taxonomy", {"search": "finch"})
    assert "House Finch" in res
    assert engine.call_count == 1
