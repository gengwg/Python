# python requests post json example

import requests
import json

# defining the api-endpoint
API_ENDPOINT = "http://example.com/API/"

# data to be sent to api
data = {
  "sourceid": "XXXService",
  "overallstatus": "amber",
  "kpidata": [
    {
      "Status": "amber",
      "Service Name": "XXXService",
      "Reported Time": "2019-08-01T18:04:26.609744551Z",
      "Value": "testalert"
    }
  ]
}

headers={"Content-Type":"application/json"}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers=headers)

# extracting response text
print r.text
