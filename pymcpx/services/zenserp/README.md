# Zenserp Service

MCP-compatible LangChain tools for the [Zenserp API](https://zenserp.com/) — Google SERP scraping with support for Images, Videos, News, Maps, Shopping, YouTube, Bing, Yandex, Google Trends, and more.

## Prerequisites

- A Zenserp API key (free tier available at [zenserp.com](https://zenserp.com/))
- Python 3.11+

## Installation

```bash
pip install pymcpx[zenserp]
```

Set your API key as an environment variable:

```bash
export ZENSERP_API_KEY="your_api_key_here"
```

## Tools

| Tool Name                          | Class                              | Description                                                          | Input Keys                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------- | ---------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `zenserp_search`                   | `ZenserpSearchTool`                | Google SERP search — web results with full parameter support         | `q`, `location`, `search_engine`, `start`, `num`, `tbm`, `device`, `timeframe`, `gl`, `hl`, `lr`, `output`, `image_url`, `ll`, `sp`, `cc`, `mkt`, `lat`, `lon`, `first`, `count`, `p`, `numdoc`, `lang`, `within`, `uule`                                                                                                                                                         |
| `zenserp_image_search`             | `ZenserpImageSearchTool`           | Google Image search                                                  | All search params (tbm preset to `isch`)                                                                                                                                                                                                                                                                                                                                            |
| `zenserp_video_search`             | `ZenserpVideoSearchTool`           | Google Video search                                                  | All search params (tbm preset to `vid`)                                                                                                                                                                                                                                                                                                                                             |
| `zenserp_news_search`              | `ZenserpNewsSearchTool`            | Google News search                                                   | All search params (tbm preset to `nws`)                                                                                                                                                                                                                                                                                                                                             |
| `zenserp_shopping_search`          | `ZenserpShoppingSearchTool`        | Google Shopping search                                               | All search params (tbm preset to `shop`)                                                                                                                                                                                                                                                                                                                                            |
| `zenserp_maps_search`              | `ZenserpMapsSearchTool`            | Google Maps / local search                                           | All search params (tbm preset to `lcl`)                                                                                                                                                                                                                                                                                                                                             |
| `zenserp_reverse_image_search`     | `ZenserpImageReverseSearchTool`    | Reverse image search by URL                                          | All search params (requires `image_url`)                                                                                                                                                                                                                                                                                                                                            |
| `zenserp_youtube_search`           | `ZenserpYouTubeSearchTool`         | YouTube search                                                       | All search params (search_engine preset to `youtube.com`)                                                                                                                                                                                                                                                                                                                           |
| `zenserp_bing_search`              | `ZenserpBingSearchTool`            | Bing search                                                          | All search params (search_engine preset to `bing.com`)                                                                                                                                                                                                                                                                                                                              |
| `zenserp_yandex_search`            | `ZenserpYandexSearchTool`          | Yandex search                                                        | All search params (search_engine preset to `yandex.com`)                                                                                                                                                                                                                                                                                                                           |
| `zenserp_shopping_product`         | `ZenserpShoppingProductTool`       | Shopping product page details                                        | `product_id`, `location`, `search_engine`, `hl`, `gl`                                                                                                                                                                                                                                                                                                                              |
| `zenserp_trends`                   | `ZenserpTrendsTool`                | Google Trends data                                                   | `keywords` (list), `cat`, `timeframe`, `type`, `hl`, `geo`                                                                                                                                                                                                                                                                                                                         |
| `zenserp_trending`                 | `ZenserpTrendingTool`              | Google Trending searches                                             | `cat`, `hl`, `geo`                                                                                                                                                                                                                                                                                                                                                                  |
| `zenserp_status`                   | `ZenserpStatusTool`                | Account status and remaining requests                                | *(none)*                                                                                                                                                                                                                                                                                                                                                                            |
| `zenserp_languages`                | `ZenserpLanguagesTool`             | Supported Google interface languages                                 | *(none)*                                                                                                                                                                                                                                                                                                                                                                            |
| `zenserp_countries`                | `ZenserpCountriesTool`             | Supported Google country codes                                       | *(none)*                                                                                                                                                                                                                                                                                                                                                                            |
| `zenserp_locations`                | `ZenserpLocationsTool`             | Supported geo locations                                              | *(none)*                                                                                                                                                                                                                                                                                                                                                                            |
| `zenserp_search_engines`           | `ZenserpSearchEnginesTool`         | Available search engines                                             | *(none)*                                                                                                                                                                                                                                                                                                                                                                            |

## Usage Examples

### Individual Tool

```python
import os
os.environ["ZENSERP_API_KEY"] = "your_key"

from pymcpx.zenserp import ZenserpSearchTool

tool = ZenserpSearchTool()
result = tool.run({"q": "latest AI news", "gl": "us", "num": 5})
print(result)
```

### Image Search

```python
from pymcpx.zenserp import ZenserpImageSearchTool

tool = ZenserpImageSearchTool()
result = tool.run({"q": "sunset landscape", "gl": "us"})
print(result)
```

### YouTube Search

```python
from pymcpx.zenserp import ZenserpYouTubeSearchTool

tool = ZenserpYouTubeSearchTool()
result = tool.run({"q": "python machine learning tutorial"})
print(result)
```

### Google Trends

```python
from pymcpx.zenserp import ZenserpTrendsTool

tool = ZenserpTrendsTool()
result = tool.run({"keywords": ["openai", "anthropic", "google"], "timeframe": "today 12-m"})
print(result)
```

### Toolkit (all tools)

```python
import os
os.environ["ZENSERP_API_KEY"] = "your_key"

from pymcpx.zenserp import ZenserpToolkit

toolkit = ZenserpToolkit()
tools = toolkit.get_tools()
results = tools[0].run({"q": "test"})
print(results)
```

### MCP Integration

```python
from pymcpx.zenserp import MCP_TOOLS

# Pass MCP_TOOLS to your MCP-compatible agent framework
for tool in MCP_TOOLS:
    print(f"{tool.name}: {tool.description}")
```
