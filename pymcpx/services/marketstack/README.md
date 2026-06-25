# Marketstack Service

MCP-compatible LangChain tools for financial market data via the [Marketstack API](https://marketstack.com).

## Prerequisites

A Marketstack API access key (free tier available). Set it in your environment:

```
MARKETSTACK_ACCESS_KEY=your_api_key_here
```

## Installation

Install the marketstack extra:

```bash
pip install pymcpx[marketstack]
```

## Tools

| Tool Name | Class | Description | Input Keys |
|-----------|-------|-------------|------------|
| `marketstack_eod` | `MarketstackEodTool` | End-of-Day stock data | `symbols` (required), `date`, `latest`, `exchange`, `date_from`, `date_to`, `sort`, `limit`, `offset` |
| `marketstack_intraday` | `MarketstackIntradayTool` | Intraday stock prices at configurable intervals | `symbols` (required), `interval`, `date`, `latest`, `exchange`, `date_from`, `date_to`, `sort`, `limit`, `offset`, `after_hours` |
| `marketstack_realtime_price` | `MarketstackRealtimePriceTool` | Real-time stock price for a single symbol | `ticker` (required), `exchange` |
| `marketstack_commodities` | `MarketstackCommoditiesTool` | Commodity prices (real-time or historical) | `commodity_name` (required), `date_from`, `date_to`, `frequency` |
| `marketstack_company_ratings` | `MarketstackCompanyRatingsTool` | Analyst buy/sell/hold ratings | `ticker` (required), `date_from`, `date_to`, `rated` |
| `marketstack_splits` | `MarketstackSplitsTool` | Stock split history | `symbols`, `symbol`, `date_from`, `date_to`, `sort`, `limit`, `offset` |
| `marketstack_dividends` | `MarketstackDividendsTool` | Dividend payment history | `symbols`, `symbol`, `date_from`, `date_to`, `sort`, `limit`, `offset` |
| `marketstack_ticker_info` | `MarketstackTickerInfoTool` | Ticker properties (sector, industry, etc.) | `symbol` (required), `exchange`, `use_tickerinfo_endpoint`, `limit`, `offset` |
| `marketstack_list_tickers` | `MarketstackListTickersTool` | Search and list stock tickers | `search`, `exchange`, `limit`, `offset` |
| `marketstack_indices` | `MarketstackIndexListTool` | Stock market index listings and details | `index`, `limit`, `offset` |
| `marketstack_exchanges` | `MarketstackExchangesTool` | Exchange details, tickers, EOD, intraday | `mic`, `endpoint_type`, `symbols`, `date`, `interval`, `date_from`, `date_to`, `sort`, `limit`, `offset`, `search` |
| `marketstack_currencies` | `MarketstackCurrenciesTool` | List supported currencies | `limit`, `offset` |
| `marketstack_timezones` | `MarketstackTimezonesTool` | List supported timezones | `limit`, `offset` |
| `marketstack_bonds` | `MarketstackBondsTool` | Government bond yields | `country`, `limit`, `offset` |
| `marketstack_etfs` | `MarketstackEtfsTool` | ETF holdings and portfolio weights | `ticker`, `list_type`, `date_from`, `date_to`, `limit`, `offset` |
| `marketstack_edgar_cik` | `MarketstackEdgarCikTool` | CIK lookup by company name or vice versa | `company_name`, `cik_code`, `limit`, `offset` |
| `marketstack_edgar_submissions` | `MarketstackEdgarSubmissionsTool` | SEC EDGAR submission histories | `cik_code`, `cik_code_name`, `report_from`, `report_to`, `filing_from`, `filing_to`, `accession_number` |
| `marketstack_edgar_facts` | `MarketstackEdgarFactsTool` | Company facts, concepts, Accounts Payable | `cik_code` (required), `query_type`, `frame`, `unit` |

## Usage

### Individual Tools

```python
from pymcpx.marketstack import MarketstackEodTool

tool = MarketstackEodTool()
result = tool.invoke({"symbols": "AAPL,MSFT", "limit": 5})
print(result)
```

### Toolkit

```python
from pymcpx.marketstack import MarketstackToolkit

toolkit = MarketstackToolkit()
tools = toolkit.get_tools()
```

### MCP Integration

Register all tools with your MCP server:

```python
from pymcpx.marketstack import MCP_TOOLS

mcp_server.register_tools(MCP_TOOLS)
```
