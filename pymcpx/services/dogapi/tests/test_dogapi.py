from httpx import Response
import respx

from pymcpx.services.dogapi import (
    DogapiSimulationEngine,
    DogapiToolkit,
    GetRandomDogImageByBreedTool,
    GetRandomDogImageTool,
    ListBreedsTool,
)


@respx.mock
def test_list_breeds_tool() -> None:
    tool = ListBreedsTool()
    assert tool.name == "list_breeds"

    respx.get("https://dog.ceo/api/breeds/list/all").mock(
        return_value=Response(
            200,
            json={
                "message": {
                    "affenpinscher": [],
                    "beagle": [],
                    "hound": ["afghan", "basset"],
                },
                "status": "success",
            },
        )
    )

    res = tool.run({"search": "hound", "limit": 5})
    assert "hound" in res
    assert "basset hound" in res


@respx.mock
def test_list_breeds_no_search() -> None:
    tool = ListBreedsTool()

    respx.get("https://dog.ceo/api/breeds/list/all").mock(
        return_value=Response(
            200,
            json={
                "message": {
                    "affenpinscher": [],
                    "beagle": [],
                    "hound": ["afghan"],
                },
                "status": "success",
            },
        )
    )

    res = tool.run({"limit": 10})
    assert "affenpinscher" in res
    assert "beagle" in res


@respx.mock
def test_get_random_dog_image_tool() -> None:
    tool = GetRandomDogImageTool()
    assert tool.name == "get_random_dog_image"

    respx.get("https://dog.ceo/api/breeds/image/random").mock(
        return_value=Response(
            200,
            json={
                "message": "https://images.dog.ceo/breeds/hound/n02088000_100.jpg",
                "status": "success",
            },
        )
    )

    res = tool.run({})
    assert res.startswith("https://images.dog.ceo")


@respx.mock
def test_get_random_dog_image_by_breed_tool() -> None:
    tool = GetRandomDogImageByBreedTool()
    assert tool.name == "get_random_dog_image_by_breed"

    respx.get("https://dog.ceo/api/breed/hound/images/random").mock(
        return_value=Response(
            200,
            json={
                "message": "https://images.dog.ceo/breeds/hound/n02088000_200.jpg",
                "status": "success",
            },
        )
    )

    res = tool.run({"breed": "hound"})
    assert "hound" in res


def test_toolkit() -> None:
    toolkit = DogapiToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 3
    names = {t.name for t in tools}
    assert "list_breeds" in names
    assert "get_random_dog_image" in names
    assert "get_random_dog_image_by_breed" in names


def test_simulation_engine() -> None:
    engine = DogapiSimulationEngine()
    engine.register(
        tool_name="list_breeds",
        input_match={"search": "hound"},
        output='["hound", "basset hound"]',
    )
    res = engine.run("list_breeds", {"search": "hound"})
    assert res == '["hound", "basset hound"]'
    assert engine.call_count == 1
