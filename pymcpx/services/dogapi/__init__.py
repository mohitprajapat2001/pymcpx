"""
pymcpx.services.dogapi
----------------------
MCP-compatible LangChain tools for the Dog CEO API.

Provides tools for:
- Listing dog breeds with fuzzy search via ``list_breeds``
- Getting a random dog image via ``get_random_dog_image``
- Getting a random dog image by breed via ``get_random_dog_image_by_breed``
"""

from pymcpx.services.dogapi.SimulationEngine import (
    DogapiSimulationEngine,
    GetRandomDogImageByBreedInput,
    GetRandomDogImageInput,
    ListBreedsInput,
)
from pymcpx.services.dogapi.tools import (
    MCP_TOOLS,
    DogapiToolkit,
    GetRandomDogImageByBreedTool,
    GetRandomDogImageTool,
    ListBreedsTool,
)

__all__ = [
    "MCP_TOOLS",
    "DogapiSimulationEngine",
    "DogapiToolkit",
    "GetRandomDogImageByBreedInput",
    "GetRandomDogImageByBreedTool",
    "GetRandomDogImageInput",
    "GetRandomDogImageTool",
    "ListBreedsInput",
    "ListBreedsTool",
]
