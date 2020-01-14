from pytest import fixture, raises

from utils import extract_nested_urls, recursive_extract_urls, search_web


@fixture
def empty_results_keywords():
    return "heldsajkhbdas sajhkdas"


@fixture
def google_results():
    return list(search_web("some keywords"))


@fixture
def url():
    return "https://www.google.com/"


@fixture
def broken_url():
    return "htt:ggle.com"
