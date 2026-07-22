import os

from httpx import Response
import respx

from pymcpx.services.screenshotlayer import (
    ScreenshotlayerCaptureTool,
    ScreenshotlayerSimulationEngine,
    ScreenshotlayerToolkit,
)

os.environ["SCREENSHOTLAYER_ACCESS_KEY"] = "mock_key"
MOCK_IMAGE_BYTES = b"\x89PNG\r\n\x1a\n" + b"\x00" * 100


@respx.mock
def test_capture_tool() -> None:
    tool = ScreenshotlayerCaptureTool()
    assert tool.name == "screenshotlayer_capture"

    request_mock = respx.get("https://api.screenshotlayer.com/api/capture").mock(
        return_value=Response(200, content=MOCK_IMAGE_BYTES)
    )

    result = tool.run({"url": "https://example.com"})
    assert result.startswith("Screenshot saved to:")
    assert result.endswith(".png")
    assert request_mock.called
    assert "access_key=mock_key" in request_mock.calls[0].request.url.query.decode("utf-8")


@respx.mock
def test_capture_tool_with_format() -> None:
    tool = ScreenshotlayerCaptureTool()

    request_mock = respx.get("https://api.screenshotlayer.com/api/capture").mock(
        return_value=Response(200, content=b"MOCK_JPEG_DATA")
    )

    result = tool.run({"url": "https://example.com", "format": "JPG"})
    assert result.endswith(".jpg")
    assert request_mock.called


@respx.mock
def test_capture_tool_error_response() -> None:
    tool = ScreenshotlayerCaptureTool()

    request_mock = respx.get("https://api.screenshotlayer.com/api/capture").mock(
        return_value=Response(
            400,
            json={
                "success": False,
                "error": {
                    "code": 210,
                    "type": "invalid_url",
                    "info": "User provided an invalid website URL.",
                },
            },
        )
    )

    result = tool.run({"url": "not-a-url"})
    assert "invalid_url" in result
    assert "invalid website URL" in result
    assert request_mock.called


def test_toolkit() -> None:
    toolkit = ScreenshotlayerToolkit()
    tools = toolkit.get_tools()
    assert len(tools) == 1
    assert tools[0].name == "screenshotlayer_capture"


def test_simulation_engine() -> None:
    engine = ScreenshotlayerSimulationEngine()
    engine.register(
        tool_name="screenshotlayer_capture",
        input_match={"url": "https://example.com"},
        output="Screenshot saved to: /tmp/mock.png",
    )
    res = engine.run("screenshotlayer_capture", {"url": "https://example.com"})
    assert res == "Screenshot saved to: /tmp/mock.png"
    assert engine.call_count == 1
