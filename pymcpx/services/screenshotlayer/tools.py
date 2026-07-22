from typing import Any

from langchain_core.tools import BaseTool
from pydantic import BaseModel

from pymcpx.services.screenshotlayer.SimulationEngine.models import (
    ScreenshotlayerCaptureInput,
)
from pymcpx.services.screenshotlayer.SimulationEngine.utils import (
    capture,
)


class ScreenshotlayerCaptureTool(BaseTool):
    """Capture website screenshots via Screenshotlayer API."""

    name: str = "screenshotlayer_capture"
    description: str = (
        "Capture a high-quality screenshot of any website URL. Returns a saved image file path. "
        "Supports PNG, JPG, GIF, WEBP formats. Can capture full-page, set custom viewport size, "
        "inject CSS, add delay for JS-heavy pages, set custom User-Agent, and more."
    )
    args_schema: type[BaseModel] = ScreenshotlayerCaptureInput

    def _run(self, **kwargs: Any) -> str:
        try:
            return capture(**kwargs)
        except Exception as exc:
            return f"Error: {exc}"


class ScreenshotlayerToolkit:
    """Convenience bundle that exposes all Screenshotlayer tools."""

    def get_tools(self) -> list[BaseTool]:
        return [ScreenshotlayerCaptureTool()]


MCP_TOOLS: list[BaseTool] = [
    ScreenshotlayerCaptureTool(),
]
