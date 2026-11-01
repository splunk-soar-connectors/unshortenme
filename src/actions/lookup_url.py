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
from urllib.parse import quote

from soar_sdk.abstract import SOARClient
from soar_sdk.action_results import ActionOutput, OutputField
from soar_sdk.logging import getLogger
from soar_sdk.params import Param, Params

from ..app import Asset, app
from ..helper import make_request

logger = getLogger()


class LookupUrlParams(Params):
    url: str = Param(
        description="URL to unshorten",
        primary=True,
        cef_types=["url", "domain"],
        column_name="Short URL",
    )


class LookupUrlOutput(ActionOutput):
    resolved_url: str | None = OutputField(column_name="Resolved URL")
    success: bool | None = None
    usage_count: str | None = None
    error: str | None = None
    requested_url: str | None = OutputField(cef_types=["url"])
    remaining_calls: float | None = OutputField(example_values=[9])


@app.action(
    name="lookup url",
    identifier="unshorten_url",
    description="Get the original URL from a shortened URL",
    action_type="investigate",
    read_only=True,
    params_class=LookupUrlParams,
    output_class=LookupUrlOutput,
    render_as="table",
)
def lookup_url(
    params: LookupUrlParams, soar: SOARClient, asset: Asset
) -> LookupUrlOutput:
    """Get the original URL from a shortened URL."""
    logger.progress("Checking URL")
    url = params.url
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        url = url[8:]

    data = make_request(quote(url, safe=""))
    if data.get("usage_count") is not None:
        data["usage_count"] = str(data["usage_count"])
    soar.set_message("Successfully unshortened the given URL")
    return LookupUrlOutput(**data)
