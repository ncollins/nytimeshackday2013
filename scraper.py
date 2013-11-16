import csv
import requests
from bs4 import BeautifulSoup
from login import keys

CSV_FILE = 'bills.csv'

ARTICLE_SEARCH_URL = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?api-key={key}'
SUNLIGHT_CONGRESS_URL = 'http://congress.api.sunlightfoundation.com/{method}?{query}&apikey={key}'

def get_json(url):
    return requests.get(url).json()

def sunlight_url(base, method, query, key):
    return base.format(method=method, query=query, key=key)

def sunlight_query(**kwargs):
    return '&'.join(key+'='+value for key,value in kwargs.items())

def save_url(url, path, name):
    file_path = path + '/' + name + '.txt'
    r = requests.get(url)
    text = BeautifulSoup(r.text).get_text()
    with open(file_path, 'w') as f:
        f.write(text)
        print('saved: ' + url + ', to: ' + file_path)
        return file_path

#qHealth = sunlight_query(congress='113', query='health care')
#bHealth = get_json(sunlight_url(SUNLIGHT_CONGRESS_URL, 'bills/search', qHealth, keys['sunlight']))

def get_bills(max_pages=50):
    loop = 0
    while loop < max_pages:
        query = sunlight_query(congress='113', per_page='50', page=str(loop))
        url = sunlight_url(SUNLIGHT_CONGRESS_URL, 'bills', query, keys['sunlight'])
        bills = get_json(url)
        for b in bills['results']:
            yield b
        loop = bills['page']['page'] + 1

def main():
    with open(CSV_FILE, 'w') as data_file:
        writer = csv.writer(data_file, delimiter=',', quotechar='|')
        for b in get_bills(max_pages=50):
            if b['history']['active'] and b.get('last_version', None):
                number = b['number']
                chamber = b['chamber']
                sponsor = b['sponsor_id']
                congress = b['congress']
                introduced_on = b['introduced_on']
                title = b['official_title']
                if b.get('last_version', None):
                    link = b['last_version']['urls']['html']
                    file_path = save_url(link, 'bill_text', str(number))
                    writer.writerow([congress, chamber, number, introduced_on,
                                     sponsor, title, file_path])

if __name__ == '__main__':
    main()
