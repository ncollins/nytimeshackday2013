import requests
from bs4 import BeautifulSoup
from login import keys

ARTICLE_SEARCH_URL = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?api-key={key}'
SUNLIGHT_CONGRESS_URL = 'http://congress.api.sunlightfoundation.com/{method}?{query}&apikey={key}'

def get_json(url):
    return requests.get(url).json()

def sunlight_url(base, method, query, key):
    return base.format(method=method, query=query, key=key)

def sunlight_query(**kwargs):
    return '&'.join(key+'='+value for key,value in kwargs.items())

def save_url(url, path, name):
    r = requests.get(url)
    text = BeautifulSoup(r.text).get_text()
    with open(path + '/' + name + '.txt', 'w') as f:
        f.write(text)
        print('saved: ' + url)


#qHealth = sunlight_query(congress='113', query='health care')
#bHealth = get_json(sunlight_url(SUNLIGHT_CONGRESS_URL, 'bills/search', qHealth, keys['sunlight']))

def get_bills(max_pages=100):
    loop = 0
    while loop < max_pages:
        query = sunlight_query(congress='113', per_page='50', page=str(loop))
        url = sunlight_url(SUNLIGHT_CONGRESS_URL, 'bills', query, keys['sunlight'])
        bills = get_json(url)
        for b in bills['results']:
            yield b
        loop = bills['page']['page'] + 1

def valid_bill(bill):
    return bill['history']['active']

def main():
    for b in get_bills(10):
        if valid_bill(b) and b.get('last_version', None):
            number = b['number']
            title = b['official_title']
            if b.get('last_version', None):
                link = b['last_version']['urls']['html']
                save_url(link, 'bill_text', str(number))
