[comment]: # "Auto-generated SOAR connector documentation"
# unshorten\.me

Publisher: Splunk  
Connector Version: 2\.0\.2  
Product Vendor: Unshorten\.me  
Product Name: Unshorten\.me  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app integrates with the unshorten\.me service to expand shortened URLs

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity\. This action runs a quick query on the server to check the connection  
[lookup url](#action-lookup-url) - Get the original URL from a shortened URL  

## action: 'test connectivity'
Validate the asset configuration for connectivity\. This action runs a quick query on the server to check the connection

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
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.parameter\.url | string |  `url`  `domain` 
action\_result\.data\.\*\.resolved\_url | string | 
action\_result\.summary | string | 
action\_result\.status | string | 
action\_result\.data\.\*\.success | boolean | 
action\_result\.data\.\*\.usage\_count | string | 
action\_result\.data\.\*\.error | string | 
action\_result\.data\.\*\.requested\_url | string |  `url` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 
action\_result\.data\.\*\.remaining\_calls | numeric | 
action\_result\.message | string | 