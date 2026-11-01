# unshorten.me

Publisher: Splunk <br>
Connector Version: 2.0.8 <br>
Product Vendor: Unshorten.me <br>
Product Name: Unshorten.me <br>
Minimum Product Version: 7.0.0

This app integrates with the unshorten.me service to expand shortened URLs

### Supported Actions

[test connectivity](#action-test-connectivity) - test connectivity <br>
[lookup url](#action-lookup-url) - Get the original URL from a shortened URL

## action: 'test connectivity'

test connectivity

Type: **test** <br>
Read only: **True**

Basic test for app.

#### Action Parameters

No parameters are required for this action

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failure |
action_result.message | string | | |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

## action: 'lookup url'

Get the original URL from a shortened URL

Type: **investigate** <br>
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** | required | URL to unshorten | string | `url` `domain` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failure |
action_result.message | string | | |
action_result.parameter.url | string | `url` `domain` | |
action_result.data.\*.resolved_url | string | | |
action_result.data.\*.success | boolean | | True False |
action_result.data.\*.usage_count | string | | |
action_result.data.\*.error | string | | |
action_result.data.\*.requested_url | string | `url` | |
action_result.data.\*.remaining_calls | numeric | | 9 |
summary.total_objects | numeric | | 1 |
summary.total_objects_successful | numeric | | 1 |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2026 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
