import requests
from bs4 import BeautifulSoup
from .settings import API_KEY, BASE_URL, ENGINE_ID


def search_web(*keywords):
    request_url = f"{BASE_URL}?key={API_KEY}&cx={ENGINE_ID}&q={' '.join(keywords)}"
    response = requests.get(request_url)
    try:
        yield from map(lambda item: item.get('link'), response.json()['items'])
    except KeyError as e:
        raise ValueError(
            f'Sorry, no results for keywords: {", ".join(keywords)}') from e


def extract_nested_urls(url):
    try:
        page = requests.get(url).text
    except requests.exceptions.ConnectionError:
        return []
    soup = BeautifulSoup(page, 'html.parser')
    all_urls = map(lambda block: block.get('href'), soup.find_all('a'))
    yield from filter(lambda link: link and link.startswith('http'), all_urls)


def recursive_extract_urls(*urls, level=0):
    for url in urls:
        print(url)
        if level <= 0:
            yield url
        elif level == 1:
            yield from extract_nested_urls(url)
        yield from recursive_extract_urls(*extract_nested_urls(url), level=level - 1)


a = search_web()
