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
from soar_sdk.abstract import SOARClient
from soar_sdk.app import App
from soar_sdk.asset import BaseAsset
from soar_sdk.exceptions import ActionFailure

from .helper import make_request


class Asset(BaseAsset):
    pass


app = App(
    name="unshorten.me",
    app_type="information",
    logo="logo_unshortenme.svg",
    logo_dark="logo_unshortenme_dark.svg",
    product_vendor="Unshorten.me",
    product_name="Unshorten.me",
    publisher="Splunk",
    appid="bd516f25-6b30-4ac9-afdf-178c576d1921",
    fips_compliant=True,
    asset_cls=Asset,
)


@app.test_connectivity()
def test_connectivity(soar: SOARClient, asset: Asset) -> None:
    data = make_request("goo.gl/IGL1lE")
    if data.get("resolved_url") != "https://unshorten.me/":
        raise ActionFailure("API returned invalid data.")
    soar.set_message("Connection successful.")


from . import actions  # noqa: F401


if __name__ == "__main__":
    app.cli()
