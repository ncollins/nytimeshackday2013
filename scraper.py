import requests
import login

ARTICLE_SEARCH_URL = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?api-key={key}'

def get_json(url, key):
    r = requests.get(url.format(key=key))
    return r.json()

print(get_json(ARTICLE_SEARCH_URL, login.keys['nyt_article_search']))
