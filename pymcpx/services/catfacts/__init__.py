"""
pymcpx.services.catfacts
------------------------
MCP-compatible LangChain tools for the Cat Fact Ninja API.

Provides tools for:
- Fetching a list of breeds via ``get_breeds``
- Fetching a random cat fact via ``get_random_fact``
- Fetching a list of cat facts via ``get_facts``
"""

from pymcpx.services.catfacts.SimulationEngine import (
    BreedModel,
    CatFactModel,
    CatfactsSimulationEngine,
    GetBreedsInput,
    GetFactsInput,
    GetRandomFactInput,
    get_breeds,
    get_facts,
    get_random_fact,
)
from pymcpx.services.catfacts.tools import (
    MCP_TOOLS,
    CatfactsToolkit,
    GetBreedsTool,
    GetFactsTool,
    GetRandomFactTool,
)

__all__ = [
    "MCP_TOOLS",
    "BreedModel",
    "CatFactModel",
    "CatfactsSimulationEngine",
    "CatfactsToolkit",
    "GetBreedsInput",
    "GetBreedsTool",
    "GetFactsInput",
    "GetFactsTool",
    "GetRandomFactInput",
    "GetRandomFactTool",
    "get_breeds",
    "get_facts",
    "get_random_fact",
]
