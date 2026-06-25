from __future__ import annotations

import json
import os
import tempfile
from typing import Any

import httpx

BASE_URL = "https://api.screenshotlayer.com/api"


def _get_access_key() -> str:
    key = os.environ.get("SCREENSHOTLAYER_ACCESS_KEY")
    if not key:
        raise ValueError(
            "SCREENSHOTLAYER_ACCESS_KEY environment variable is not set. "
            "Please set it to your Screenshotlayer API access key."
        )
    return key


def _build_params(access_key: str, **kwargs: Any) -> dict[str, Any]:
    params: dict[str, Any] = {"access_key": access_key}
    for k, v in kwargs.items():
        if v is not None:
            if k == "format":
                params[k] = v.lower()
            elif k == "scale":
                if v == 1:
                    continue
                params[k] = str(v)
            elif k == "placeholder":
                if v in ("1", "true"):
                    params[k] = "1"
                else:
                    params[k] = v
            else:
                params[k] = v
    return params


def _get_extension(fmt: str | None) -> str:
    ext_map = {"PNG": ".png", "JPG": ".jpg", "JPEG": ".jpg", "GIF": ".gif", "WEBP": ".webp"}
    return ext_map.get(fmt.upper() if fmt else "PNG", ".png")


def capture(**kwargs: Any) -> str:
    """Capture a website screenshot and save it to a temporary file."""
    access_key = _get_access_key()
    params = _build_params(access_key, **kwargs)
    url = f"{BASE_URL}/capture"

    with httpx.Client() as client:
        response = client.get(url, params=params, timeout=60)

    if response.status_code != 200:
        try:
            err_data = response.json()
            return json.dumps(err_data, indent=2, ensure_ascii=False)
        except (json.JSONDecodeError, ValueError):
            return (
                f"Error: Screenshotlayer API returned HTTP {response.status_code} — "
                f"{response.text}"
            )

    fmt = kwargs.get("format", "PNG")
    ext = _get_extension(fmt)

    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(response.content)
        tmp_path = tmp.name

    return f"Screenshot saved to: {tmp_path}"
