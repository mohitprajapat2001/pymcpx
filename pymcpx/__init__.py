"""
PyMCPX — MCP-compatible LangChain tools for AI agents.

Quick start
-----------
Install a service extra:
    pip install pymcpx[calculator]

Import tools:
    from pymcpx.calculator import AddTool

Or import all tools from a service:
    from pymcpx.calculator import *
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pymcpx")
except PackageNotFoundError:  # running from source without installation
    __version__ = "0.0.0.dev0"

__all__ = ["__version__"]
