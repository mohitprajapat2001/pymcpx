"""
PyMCPX — MCP-compatible LangChain tools for popular services.

Quick start
-----------
Install a service extra:
    pip install pymcpx[github]

Import tools:
    from pymcpx.services.github import GitHubSearchRepositoriesTool

Or import all tools from a service:
    from pymcpx.services.github import *
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pymcpx")
except PackageNotFoundError:  # running from source without installation
    __version__ = "0.0.0.dev0"

__all__ = ["__version__"]
