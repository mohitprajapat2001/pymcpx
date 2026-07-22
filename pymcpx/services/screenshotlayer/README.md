# Screenshotlayer Service

MCP-compatible LangChain tools for the [Screenshotlayer API](https://screenshotlayer.com/) — capture high-quality website screenshots as PNG, JPEG, GIF, or WEBP.

## Prerequisites

- A Screenshotlayer API access key (free tier available at [screenshotlayer.com](https://screenshotlayer.com/))
- Python 3.11+

## Installation

```bash
pip install pymcpx[screenshotlayer]
```

Set your API key as an environment variable:

```bash
export SCREENSHOTLAYER_ACCESS_KEY="your_api_key_here"
```

## Tools

| Tool Name                     | Class                          | Description                                              | Input Keys                                                                                                                                                                  |
| ----------------------------- | ------------------------------ | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `screenshotlayer_capture`     | `ScreenshotlayerCaptureTool`   | Capture a website screenshot as an image file            | `url`, `format`, `fullpage`, `width`, `viewport`, `css_url`, `delay`, `ttl`, `force`, `placeholder`, `user_agent`, `accept_lang`, `export`, `secret_key`, `scale`, `quality` |

## Usage Examples

### Individual Tool

```python
import os
os.environ["SCREENSHOTLAYER_ACCESS_KEY"] = "your_key"

from pymcpx.screenshotlayer import ScreenshotlayerCaptureTool

tool = ScreenshotlayerCaptureTool()
result = tool.run({"url": "https://example.com", "fullpage": 1, "viewport": "1920x1080"})
print(result)
# Screenshot saved to: /tmp/tmpXXXXX.png
```

### Capture as JPEG with custom settings

```python
tool = ScreenshotlayerCaptureTool()
result = tool.run({
    "url": "https://www.apple.com",
    "format": "JPG",
    "width": 800,
    "delay": 3,
    "quality": 85,
})
print(result)
```

### Toolkit (all tools)

```python
import os
os.environ["SCREENSHOTLAYER_ACCESS_KEY"] = "your_key"

from pymcpx.screenshotlayer import ScreenshotlayerToolkit

toolkit = ScreenshotlayerToolkit()
tools = toolkit.get_tools()
result = tools[0].run({"url": "https://example.com"})
print(result)
```

### MCP Integration

```python
from pymcpx.screenshotlayer import MCP_TOOLS

# Pass MCP_TOOLS to your MCP-compatible agent framework
for tool in MCP_TOOLS:
    print(f"{tool.name}: {tool.description}")
```
