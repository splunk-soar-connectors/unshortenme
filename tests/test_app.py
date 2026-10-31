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
import httpx
import pytest
from soar_sdk.exceptions import ActionFailure

from src.helper import make_request


def test_make_request_returns_json(monkeypatch: pytest.MonkeyPatch) -> None:
    expected = {"resolved_url": "https://example.com", "usage_count": 1}
    response = httpx.Response(
        200,
        headers={"Content-Type": "application/json"},
        json=expected,
        request=httpx.Request("GET", "https://unshorten.me/json/example.com"),
    )
    monkeypatch.setattr(httpx, "get", lambda *args, **kwargs: response)

    assert make_request("example.com") == expected


def test_make_request_raises_for_api_error(monkeypatch: pytest.MonkeyPatch) -> None:
    response = httpx.Response(
        200,
        headers={"Content-Type": "application/json"},
        json={"error": "Invalid URL"},
        request=httpx.Request("GET", "https://unshorten.me/json/invalid"),
    )
    monkeypatch.setattr(httpx, "get", lambda *args, **kwargs: response)

    with pytest.raises(ActionFailure, match="API returned error: Invalid URL"):
        make_request("invalid")
