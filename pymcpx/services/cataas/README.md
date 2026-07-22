# Cataas Service

MCP-compatible LangChain tools for cat images via the [Cat as a Service (CATAAS) API](https://cataas.com).

## Prerequisites

No API key required — the CATAAS API is free and open.

## Installation

Install the cataas extra:

```bash
pip install pymcpx[cataas]
```

## Tools

| Tool Name | Class | Description | Input Keys |
|-----------|-------|-------------|------------|
| `list_tags` | `ListTagsTool` | List tags with optional fuzzy search | `search` (optional), `limit` (default 20) |
| `list_cats` | `ListCatsTool` | List cats with tag filter and fuzzy search | `limit` (default 10), `skip`, `tags`, `search` |
| `count_cats` | `CountCatsTool` | Count all cats | — |
| `get_random_cat` | `GetRandomCatTool` | Random cat image or JSON | `transform` |
| `get_cat_by_id` | `GetCatByIdTool` | Cat image by ID | `id`, `transform` |
| `get_cat_by_tag` | `GetCatByTagTool` | Random cat by tag | `tag`, `transform` |
| `get_random_cat_saying` | `GetRandomCatSayingTool` | Random cat with text overlay | `text`, `transform`, `text_overlay` |
| `get_cat_by_id_saying` | `GetCatByIdSayingTool` | Cat by ID with text overlay | `id`, `text`, `transform`, `text_overlay` |
| `get_random_cat_by_tag_saying` | `GetRandomCatByTagSayingTool` | Random cat by tag with text overlay | `tag`, `text`, `transform`, `text_overlay` |

The `transform` parameter accepts image options (type, filter, fit, position, width, height, blur, r/g/b, brightness, saturation, hue, lightness, html, json).
The `text_overlay` parameter accepts text options (font, font_size, font_color, font_background).

## Usage

### Individual Tools

```python
    from pymcpx.cataas import GetRandomCatTool

tool = GetRandomCatTool()
url = tool.invoke({"transform": {"width": 400, "height": 300}})
print(url)
```

### Toolkit

```python
    from pymcpx.cataas import CataasToolkit

toolkit = CataasToolkit()
tools = toolkit.get_tools()
```

### MCP Integration

```python
    from pymcpx.cataas import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```
