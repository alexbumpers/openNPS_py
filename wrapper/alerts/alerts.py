import requests
import json
from keys import NPSSecretKey


class NPS_Alerts_Write_Options(object):
    def __init__(self):
        """ Change this to TRUE if you need to write JSON data to file."""
        self.WRITE_TO_FILE = False


class NPS_Alerts(object):

    def yosemite_alerts_danger(url):
        payload = {'category':'danger'} # From /Alerts/ GET category -> danger
        alert_url = requests.get(
            "https://developer.nps.gov/api/v0/alerts",
            headers={'Authorization': NPSSecretKey.key}, params=payload)
        write = NPS_Alerts_Write_Options()
        if write.WRITE_TO_FILE == True:
            with open("alert.txt", "w") as outfile:
                alert_dump = json.dump(
                alert_url.json(),
                outfile,
                sort_keys = True,
                indent = 4,
                ensure_ascii=False)
        alert_dump = alert_url.json()
        return alert_dump
    yosemite_alerts_danger("https://developer.nps.gov/api/v0/alerts")

    


















    # def yellowstone_alerts(url):
    #     alert_url = requests.get(
    #         "https://developer.nps.gov/api/v0/alerts?parkCode=yell",
    #         headers={'Authorization': NPSSecretKey.key})
    #     return alert_url.text
