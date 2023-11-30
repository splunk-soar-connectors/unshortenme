[comment]: # "Auto-generated SOAR connector documentation"
# unshorten.me

Publisher: Splunk  
Connector Version: 2.0.5  
Product Vendor: Unshorten.me  
Product Name: Unshorten.me  
Product Version Supported (regex): ".\*"  
Minimum Product Version: 4.9.39220  

This app integrates with the unshorten.me service to expand shortened URLs

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity. This action runs a quick query on the server to check the connection  
[lookup url](#action-lookup-url) - Get the original URL from a shortened URL  

## action: 'test connectivity'
Validate the asset configuration for connectivity. This action runs a quick query on the server to check the connection

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'lookup url'
Get the original URL from a shortened URL

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | URL to unshorten | string |  `url`  `domain` 

#### Action Output
DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.parameter.url | string |  `url`  `domain`  |  
action_result.data.\*.resolved_url | string |  |  
action_result.summary | string |  |  
action_result.status | string |  |   success  failed 
action_result.data.\*.success | boolean |  |  
action_result.data.\*.usage_count | string |  |  
action_result.data.\*.error | string |  |  
action_result.data.\*.requested_url | string |  `url`  |  
summary.total_objects | numeric |  |  
summary.total_objects_successful | numeric |  |  
action_result.data.\*.remaining_calls | numeric |  |   9 
action_result.message | string |  |  