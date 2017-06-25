import requests
import json
from keys import NPSSecretKey


params = {"parkCode":"yell"}
params_json = json.dumps(params)
r = requests.get("https://developer.nps.gov/api/v0/alerts?parkCode=yell,yose",
headers={'Authorization': NPSSecretKey.key})


print(r.status_code)
print(r.text)
