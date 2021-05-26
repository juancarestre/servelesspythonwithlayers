import requests

def doreq(url):
    r = requests.get(url)
    return r