"""
Generate a new PyMCPX service skeleton.

Usage:
    python generate_service.py <snake_case_name> [--type api|simulation]

Example:
    python generate_service.py myapi
    python generate_service.py myapi --type api
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent


def snake_to_pascal(name: str) -> str:
    return "".join(word.capitalize() for word in name.split("_"))


def _tools_content(name: str, pascal: str) -> str:
    return (
        f'"""LangChain BaseTool subclasses for the {name} service."""\n'
        "\n"
        "from __future__ import annotations\n"
        "\n"
        "from typing import Any\n"
        "\n"
        "from langchain_core.tools import BaseTool\n"
        "from pydantic import BaseModel  # noqa: TC002\n"
        "\n"
        f"# from pymcpx.services.{name}.SimulationEngine.models import ...\n"
        f"# from pymcpx.services.{name}.SimulationEngine.utils import ...\n"
        "\n"
        "\n"
        f"class {pascal}Toolkit:\n"
        f'    """Convenience bundle that exposes all {name} tools."""\n'
        "\n"
        "    def get_tools(self) -> list[BaseTool]:\n"
        f'        """Return a list of every {name} tool instance."""\n'
        "        return []\n"
        "\n"
        "\n"
        "MCP_TOOLS: list[BaseTool] = [\n"
        "]\n"
    )


def _shim_content(name: str, desc: str) -> str:
    return (
        f'"""pymcpx.{name} - MCP-compatible LangChain tools for {desc}.\n'
        "\n"
        f"Re-exports from ``pymcpx.services.{name}`` for convenient access via\n"
        f"``from pymcpx.{name} import ...``.\n"
        '"""\n'
        "\n"
        f"from pymcpx.services.{name} import (\n"
        "    MCP_TOOLS,\n"
        ")\n"
        "\n"
        "__all__ = [\n"
        '    "MCP_TOOLS",\n'
        "]\n"
    )


def _engine_content(name: str, engine_cls: str) -> str:
    return (
        f'"""{engine_cls} - offline execution and simulation layer for the {name} service."""\n'
        "\n"
        "from __future__ import annotations\n"
        "\n"
        "from typing import Any\n"
        "\n"
        f"# from pymcpx.services.{name}.tools import ...\n"
        "\n"
        "\n"
        "_TOOL_REGISTRY: dict[str, Any] = {}\n"
        "\n"
        "\n"
        f"class {engine_cls}:\n"
        f'    """Offline simulation engine for the {name} service."""\n'
        "\n"
        "    def __init__(self) -> None:\n"
        "        self._fixtures: list[dict[str, Any]] = []\n"
        "        self.history: list[dict[str, Any]] = []\n"
        "\n"
        "    def register(\n"
        "        self,\n"
        "        tool_name: str,\n"
        "        output: str,\n"
        "        input_match: dict[str, Any] | None = None,\n"
        "    ) -> None:\n"
        '        """Register a canned fixture response."""\n'
        "        self._fixtures.append({\n"
        '            "tool_name": tool_name,\n'
        '            "input_match": input_match or {},\n'
        '            "output": output,\n'
        "        })\n"
        "\n"
        "    def run(self, tool_name: str, inputs: dict[str, Any] | None = None) -> str:\n"
        f'        """Run a {name} tool by name, checking fixtures first."""\n'
        "        inputs = inputs or {}\n"
        "\n"
        "        for fixture in self._fixtures:\n"
        '            if fixture["tool_name"] == tool_name and _inputs_match(\n'
        '                inputs, fixture["input_match"]\n'
        "            ):\n"
        '                call = {"tool_name": tool_name, "inputs": inputs, "output": fixture["output"]}\n'
        "                self.history.append(call)\n"
        '                return fixture["output"]\n'
        "\n"
        "        tool = _TOOL_REGISTRY.get(tool_name)\n"
        "        if tool is None:\n"
        '            available = ", ".join(sorted(_TOOL_REGISTRY))\n'
        "            raise ValueError(f\"Unknown tool '{tool_name}'. Available tools: {available}\")\n"
        "\n"
        "        output: str = tool._run(**inputs)\n"
        '        call = {"tool_name": tool_name, "inputs": inputs, "output": output}\n'
        "        self.history.append(call)\n"
        "        return output\n"
        "\n"
        "    def reset(self) -> None:\n"
        '        """Clear call history and registered fixtures."""\n'
        "        self._fixtures.clear()\n"
        "        self.history.clear()\n"
        "\n"
        "    @property\n"
        "    def call_count(self) -> int:\n"
        '        """Total number of run() calls recorded."""\n'
        "        return len(self.history)\n"
        "\n"
        "    def calls_for(self, tool_name: str) -> list[dict[str, Any]]:\n"
        '        """Return all recorded calls for a specific tool."""\n'
        '        return [c for c in self.history if c["tool_name"] == tool_name]\n'
        "\n"
        "    @staticmethod\n"
        "    def available_tools() -> list[str]:\n"
        '        """Return sorted list of all registered tool names."""\n'
        "        return sorted(_TOOL_REGISTRY)\n"
        "\n"
        "\n"
        "def _inputs_match(candidate: dict[str, Any], match: dict[str, Any]) -> bool:\n"
        '    """Return True when all key-value pairs in match appear in candidate."""\n'
        "    return all(candidate.get(k) == v for k, v in match.items())\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a new PyMCPX service skeleton")
    parser.add_argument("name", help="Service name in snake_case (e.g. my_api)")
    parser.add_argument(
        "--type",
        choices=["api", "simulation"],
        default="simulation",
        help="Service type. 'api' adds httpx dependency.",
    )
    args = parser.parse_args()

    name: str = args.name.strip().lower().replace("-", "_")
    if not re.match(r"^[a-z][a-z0-9_]*$", name):
        sys.exit(f"Error: service name must be snake_case, got '{name}'")

    Pascal = snake_to_pascal(name)
    desc = name.replace("_", " ").title()
    engine_cls = f"{Pascal}SimulationEngine"

    # --- Paths ---
    svc_dir = ROOT / "pymcpx" / "services" / name
    sim_dir = svc_dir / "SimulationEngine"
    test_dir = svc_dir / "tests"
    demo_dir = ROOT / "demos" / name
    shim_path = ROOT / "pymcpx" / f"{name}.py"

    if svc_dir.exists():
        sys.exit(f"Error: service '{name}' already exists at {svc_dir}")

    svc_dir.mkdir(parents=True)
    sim_dir.mkdir()
    test_dir.mkdir()
    demo_dir.mkdir(parents=True)

    # ---------------------- SimulationEngine/models.py ----------------------
    (sim_dir / "models.py").write_text(
        f'"""Pydantic input models for the {name} service tools."""\n',
        encoding="utf-8",
    )

    # ---------------------- SimulationEngine/utils.py -----------------------
    (sim_dir / "utils.py").write_text(
        f'"""Business logic / API client helpers for the {name} service."""\n',
        encoding="utf-8",
    )

    # ---------------------- SimulationEngine/engine.py ----------------------
    (sim_dir / "engine.py").write_text(
        _engine_content(name, engine_cls),
        encoding="utf-8",
    )

    # ---------------------- SimulationEngine/__init__.py --------------------
    (sim_dir / "__init__.py").write_text(
        f'"""Simulation layer exports for the {name} service."""\n',
        encoding="utf-8",
    )

    # ---------------------- tests/__init__.py -------------------------------
    (test_dir / "__init__.py").write_text("", encoding="utf-8")

    # ---------------------- tools.py ----------------------------------------
    (svc_dir / "tools.py").write_text(
        _tools_content(name, Pascal),
        encoding="utf-8",
    )

    # ---------------------- __init__.py (service) ---------------------------
    (svc_dir / "__init__.py").write_text(
        f'"""pymcpx.services.{name} - MCP-compatible LangChain tools for {desc}."""\n',
        encoding="utf-8",
    )

    # ---------------------- README.md ---------------------------------------
    (svc_dir / "README.md").write_text(
        f"# {desc}\n\nMCP-compatible LangChain tools for {desc}.\n",
        encoding="utf-8",
    )

    # ---------------------- pymcpx/<name>.py shim ---------------------------
    shim_path.write_text(
        _shim_content(name, desc),
        encoding="utf-8",
    )

    # ---------------------- Update pyproject.toml ---------------------------
    pyproject_path = ROOT / "pyproject.toml"
    content = pyproject_path.read_text(encoding="utf-8")

    deps = '"langchain-core>=0.2",'
    if args.type == "api":
        deps += '\n    "httpx>=0.27",'

    extra = f"{name} = [\n    {deps}\n]"

    if "# Install all services" in content:
        content = content.replace("# Install all services", f"{extra}\n# Install all services")
        all_start = content.index("all = [")
        all_close = content.index("\n]", all_start)
        content = (
            content[:all_close] + '\n{}"pymcpx[{}]",'.format("    ", name) + content[all_close:]
        )

    pyproject_path.write_text(content, encoding="utf-8")

    # ---------------------- Summary -----------------------------------------
    print(f"Created service '{name}'")
    print(f"  {svc_dir}")
    print(f"  {shim_path}")
    print(f"  {demo_dir}")
    print("pyproject.toml updated")


if __name__ == "__main__":
    main()
