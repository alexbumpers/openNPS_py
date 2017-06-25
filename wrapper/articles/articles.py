import requests
import json
from keys import NPSSecretKey


class NPS_Articles_Write_Options(object):
    def __init__(self):
        """ Change this to TRUE if you need to write JSON data to file."""
        self.WRITE_TO_FILE = True


class NPS_Articles(object):
    """
    The NPS API does not seem to support seperating by category natively.
    You can, however, parse this information via the JSON data output.
    """
    def articles_id(api_url):
        payload = {
        'id':'true'
        }
        articles_url = requests.get(
            "https://developer.nps.gov/api/v0/articles",
            headers={'Authorization': NPSSecretKey.key}, params=payload)
        write = NPS_Articles_Write_Options()
        if write.WRITE_TO_FILE == True:
            with open("articles_id.json", "w") as outfile:
                article_dump = json.dump(
                articles_url.json(),
                outfile,
                sort_keys = True,
                indent = 4,
                ensure_ascii=False)
        articles_dump = articles_url.json()
        return articles_dump
    articles_id("https://developer.nps.gov/api/v0/articles")
