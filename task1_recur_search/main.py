import argparse
import requests
from bs4 import BeautifulSoup
from itertools import islice

API_KEY = 'AIzaSyB5KBYefmCzfLoAhMROp_JmMxdYicToldo'
BASE_URL = 'https://www.googleapis.com/customsearch/v1'
ENGINE_ID = '012675951959685604488:e0emphdfbg8'


def search_web(*keywords):
    request_url = f"{BASE_URL}?key={API_KEY}&cx={ENGINE_ID}&q={' '.join(keywords)}"
    response = requests.get(request_url)
    yield from map(lambda item: item.get('link'), response.json()['items'])


"""
def mock_search_web(*keywords):
    links = ['https://www.maliburumdrinks.com/us/where-to-buy/',
            ]
    yield from map(lambda x: x, links)
"""


def extract_nested_urls(url):
    try:
        page = requests.get(url).text
    except requests.exceptions.ConnectionError:
        return []
    soup = BeautifulSoup(page, 'html.parser')
    all_urls = map(lambda block: block.get('href'), soup.find_all('a'))
    yield from filter(lambda link: getattr(link, 'startswith', lambda _: False)('http'), all_urls)


def recursive_extract(*urls, level=0):
    for url in urls:
        if level <= 0:
            yield url
        elif level == 1:
            yield from extract_nested_urls(url)
        else:
            yield from recursive_extract(*extract_nested_urls(url), level=level - 1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('keywords', help='strings passed to google search', nargs='+')
    parser.add_argument('-l', '--limit', help='maximum count of urls to display', default=10 ** 3, type=int,
                        required=False)
    parser.add_argument('-r', '--recursion', help='level of recursion to search through pages', default=0, type=int,
                        required=False)
    args = parser.parse_args()

    search_results = search_web(*args.keywords)
    nested_urls = recursive_extract(*search_results, level=args.recursion)

    for count, url in enumerate(islice(nested_urls, args.limit)):
        print(f"{count}\t{url}")
