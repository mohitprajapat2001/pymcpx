# PyMCPX v0.2.0

MCP-compatible LangChain tools for AI agents — calculator, datetime, converter, and more.

## What's New

### New Services

| Service | Install | Description |
|---------|---------|-------------|
| **Cataas** | `pymcpx[cataas]` | Cat as a Service — random cat images, GIFs, tagged/says text |
| **Catfacts** | `pymcpx[catfacts]` | Random cat facts from Cat Fact Ninja |
| **Dogapi** | `pymcpx[dogapi]` | Random dog images by breed from Dog CEO |
| **Ebird** | `pymcpx[ebird]` | Bird observations, species, taxonomy, and hotspots from eBird |

### Improvements

- **Ebird consolidated** into a single `ebird` tool with an `action` parameter (6 endpoints, one tool) — reduces LLM function-calling surface area
- **Flat param schemas** for all services with aliased fields — fixes Groq LLM compatibility
- **Fuzzy search** on taxonomy and species list endpoints
- **Limit guards** on all list endpoints (default 50, max 200)
- **Auth documentation** added to all service READMEs

## Full Service List

| Service | Auth | Install |
|---------|------|---------|
| Aviationstack | API Key | `pymcpx[aviationstack]` |
| Calculator | None | `pymcpx[calculator]` |
| Cataas | None | `pymcpx[cataas]` |
| Catfacts | None | `pymcpx[catfacts]` |
| Converter | None | `pymcpx[converter]` |
| Datetime | None | `pymcpx[datetime]` |
| Dogapi | None | `pymcpx[dogapi]` |
| Ebird | API Key | `pymcpx[ebird]` |
| ExchangeRate.host | API Key | `pymcpx[exchangeratehost]` |
| Fixer | API Key | `pymcpx[fixer]` |
| IPstack | API Key | `pymcpx[ipstack]` |
| Marketstack | API Key | `pymcpx[marketstack]` |
| Numverify | API Key | `pymcpx[numverify]` |
| Screenshotlayer | API Key | `pymcpx[screenshotlayer]` |
| Weatherstack | API Key | `pymcpx[weatherstack]` |
| Zenserp | API Key | `pymcpx[zenserp]` |

## Installation

```bash
pip install pymcpx
```

Or install with all services:

```bash
pip install "pymcpx[all]"
```
