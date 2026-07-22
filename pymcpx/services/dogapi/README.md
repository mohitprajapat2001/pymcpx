# Dogapi Service

MCP-compatible LangChain tools for dog images via the [Dog CEO API](https://dog.ceo).

## Prerequisites

No API key required — the Dog CEO API is free and open.

## Installation

Install the dogapi extra:

```bash
pip install pymcpx[dogapi]
```

## Tools

| Tool Name | Class | Description | Input Keys |
|-----------|-------|-------------|------------|
| `list_breeds` | `ListBreedsTool` | List breeds with optional fuzzy search | `search` (optional), `limit` (default 20) |
| `get_random_dog_image` | `GetRandomDogImageTool` | Random dog image URL | — |
| `get_random_dog_image_by_breed` | `GetRandomDogImageByBreedTool` | Random dog image URL by breed | `breed` |

## Usage

### Individual Tools

```python
    from pymcpx.dogapi import GetRandomDogImageTool

tool = GetRandomDogImageTool()
url = tool.invoke({})
print(url)
```

### Toolkit

```python
    from pymcpx.dogapi import DogapiToolkit

toolkit = DogapiToolkit()
tools = toolkit.get_tools()
```

### MCP Integration

```python
    from pymcpx.dogapi import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```
