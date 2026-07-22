"""
pymcpx.cataas — MCP-compatible LangChain tools for the Cat as a Service (CATAAS) API.

Re-exports from ``pymcpx.services.cataas`` for convenient access via
``from pymcpx.cataas import GetRandomCatTool``.

The original ``from pymcpx.services.cataas import ...`` path also works.
"""

from pymcpx.services.cataas import (
    MCP_TOOLS,
    CataasSimulationEngine,
    CataasToolkit,
    CatCountModel,
    CatModel,
    CountCatsInput,
    CountCatsTool,
    GetCatByIdInput,
    GetCatByIdSayingInput,
    GetCatByIdSayingTool,
    GetCatByIdTool,
    GetCatByTagInput,
    GetCatByTagTool,
    GetRandomCatByTagSayingInput,
    GetRandomCatByTagSayingTool,
    GetRandomCatInput,
    GetRandomCatSayingInput,
    GetRandomCatSayingTool,
    GetRandomCatTool,
    ListCatsInput,
    ListCatsTool,
    ListTagsInput,
    ListTagsTool,
)

__all__ = [
    "MCP_TOOLS",
    "CatCountModel",
    "CatModel",
    "CataasSimulationEngine",
    "CataasToolkit",
    "CountCatsInput",
    "CountCatsTool",
    "GetCatByIdInput",
    "GetCatByIdSayingInput",
    "GetCatByIdSayingTool",
    "GetCatByIdTool",
    "GetCatByTagInput",
    "GetCatByTagTool",
    "GetRandomCatByTagSayingInput",
    "GetRandomCatByTagSayingTool",
    "GetRandomCatInput",
    "GetRandomCatSayingInput",
    "GetRandomCatSayingTool",
    "GetRandomCatTool",
    "ListCatsInput",
    "ListCatsTool",
    "ListTagsInput",
    "ListTagsTool",
]
