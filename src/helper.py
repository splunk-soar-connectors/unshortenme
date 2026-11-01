# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Any

from soar_sdk.exceptions import ActionFailure

UNSHORTEN_ME_BASE_URL = "https://unshorten.me/json/"


def make_request(endpoint: str) -> dict[str, Any]:
    import httpx  # noqa: PLC0415

    url = UNSHORTEN_ME_BASE_URL + endpoint
    try:
        response = httpx.get(url, timeout=30)
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        response_text = e.response.text.replace("{", "{{").replace("}", "}}")
        message = f"Error response from server. Status code: {e.response.status_code}Response: {response_text}"
        raise ActionFailure(message) from e
    except httpx.RequestError as e:
        raise ActionFailure(f"Error connecting to the url ({url})") from e

    content_type = response.headers.get("Content-Type", "")
    if "html" not in content_type and "json" not in content_type:
        response_text = response.text.replace("{", "{{").replace("}", "}}")
        raise ActionFailure(f"Unexpected response from server: {response_text}")

    try:
        data = response.json()
    except ValueError as e:
        raise ActionFailure(f"Error response from server: {response.text}") from e

    if "error" in data:
        raise ActionFailure(f"API returned error: {data['error']}")

    return data
