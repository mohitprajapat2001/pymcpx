"""
pymcpx.services.cataas
----------------------
MCP-compatible LangChain tools for the Cat as a Service (CATAAS) API.

Provides tools for:
- Listing cat tags with fuzzy search via ``list_tags``
- Listing cats with tag filtering and fuzzy search via ``list_cats``
- Counting cats via ``count_cats``
- Fetching cat images with transformation options
"""

from pymcpx.services.cataas.SimulationEngine import (
    CataasSimulationEngine,
    CatCountModel,
    CatModel,
    CountCatsInput,
    GetCatByIdInput,
    GetCatByIdSayingInput,
    GetCatByTagInput,
    GetRandomCatByTagSayingInput,
    GetRandomCatInput,
    GetRandomCatSayingInput,
    ListCatsInput,
    ListTagsInput,
    count_cats,
    list_cats,
    list_tags,
)
from pymcpx.services.cataas.tools import (
    MCP_TOOLS,
    CataasToolkit,
    CountCatsTool,
    GetCatByIdSayingTool,
    GetCatByIdTool,
    GetCatByTagTool,
    GetRandomCatByTagSayingTool,
    GetRandomCatSayingTool,
    GetRandomCatTool,
    ListCatsTool,
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
    "count_cats",
    "list_cats",
    "list_tags",
]
