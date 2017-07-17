import requests
import json
from keys import NPSSecretKey


class NPS_Alerts_Write_Options(object):
    def __init__(self):
        """ Change this to TRUE if you need to write JSON data to file."""
        self.WRITE_TO_FILE = False


class NPS_Alerts(object):
    """
    Query NPS API for *all* park alerts.
    """
    def alerts(api_url):
        alert_url = requests.get(
            "https://developer.nps.gov/api/v0/alerts",
            headers={'Authorization': NPSSecretKey.key})
        write = NPS_Alerts_Write_Options()
        if write.WRITE_TO_FILE == True:
            with open("alerts.json", "w") as outfile:
                alert_dump = json.dump(
                alert_url.json(),
                outfile,
                sort_keys = True,
                indent = 4,
                ensure_ascii=False)
        alert_dump = alert_url.json()
        return alert_dump
    alerts("https://developer.nps.gov/api/v0/alerts")
