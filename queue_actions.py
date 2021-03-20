import requests
import time
import sys

def count_words_at_url(url):
    resp = requests.get(url)
    d = len(resp.text.split())
    time.sleep(90)
    print("Number of words on {0}: {1}".format(url, d))
    return d
