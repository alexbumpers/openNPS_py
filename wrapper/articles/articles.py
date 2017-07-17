import requests
import json
from keys import NPSSecretKey


class NPS_Articles_Write_Options(object):
    def __init__(self):
        """ Change this to TRUE if you need to write JSON data to file."""
        self.WRITE_TO_FILE = False


class NPS_Articles(object):
    """
    Query NPS API for *all* park articles.
    """
    def articles(api_url):
        articles_url = requests.get(
            "https://developer.nps.gov/api/v0/articles",
            headers={'Authorization': NPSSecretKey.key})
        write = NPS_Articles_Write_Options()
        if write.WRITE_TO_FILE == True:
            with open("articles.json", "w") as outfile:
                article_dump = json.dump(
                articles_url.json(),
                outfile,
                sort_keys = True,
                indent = 4,
                ensure_ascii=False)
        articles_dump = articles_url.json()
        return articles_dump
    articles("https://developer.nps.gov/api/v0/articles")
