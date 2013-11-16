import requests
from login import keys

ARTICLE_SEARCH_URL = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?api-key={key}'
SUNLIGHT_CONGRESS_URL = 'http://congress.api.sunlightfoundation.com/{method}?apikey={key}'

def get_json(url):
    return requests.get(url).json()

def sunlight_url(base, method, key):
    return base.format(method=method, key=key)

print(get_json(sunlight_url(SUNLIGHT_CONGRESS_URL, 'bills', keys['sunlight'])))
