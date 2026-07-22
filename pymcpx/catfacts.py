"""
pymcpx.catfacts — MCP-compatible LangChain tools for the Cat Fact Ninja API.

Re-exports from ``pymcpx.services.catfacts`` for convenient access via
``from pymcpx.catfacts import GetRandomFactTool``.

The original ``from pymcpx.services.catfacts import ...`` path also works.
"""

from pymcpx.services.catfacts import (
    MCP_TOOLS,
    BreedModel,
    CatFactModel,
    CatfactsSimulationEngine,
    CatfactsToolkit,
    GetBreedsInput,
    GetBreedsTool,
    GetFactsInput,
    GetFactsTool,
    GetRandomFactInput,
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
]
