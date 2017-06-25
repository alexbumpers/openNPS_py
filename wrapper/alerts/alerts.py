import requests
import json
from keys import NPSSecretKey


class NPS_Alerts_Write_Options(object):
    def __init__(self):
        """ Change this to TRUE if you need to write JSON data to file."""
        self.WRITE_TO_FILE = False


class NPS_Alerts(object):
    """
    The NPS API does not seem to support seperating by category natively.
    You can, however, parse this information via the JSON data output.
    """
    def alerts_category(api_url):
        payload = {
        'category':'Danger', # From /Alerts/ GET category -> danger
        'category':'caution', # From /Alerts/ GET category -> caution
        'category':'information', # From /Alerts/ GET category -> information
        'category':'park closure' # From /Alerts/ GET category -> park closure
        }
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
    alerts_category_danger("https://developer.nps.gov/api/v0/alerts")
