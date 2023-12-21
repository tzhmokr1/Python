import requests
import json
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()	#disables self signed certificate errors

url = 'https://192.168.1.12/api/monitoring/device/components/version'
auth = HTTPBasicAuth('cisco', 'cisco')

response = requests.get( url,  verify=False, auth=auth)

if response.status_code == 200:
    print 'Status Code: ' + str(response.status_code)	#'response.status_code' in String umwandeln
    parse = json.loads(response.text)	#load string in json object
    print json.dumps(parse, indent=4)	#pretty print
else:
    print 'ERROR Code: ' + str(response.status_code)
