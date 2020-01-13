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


def test_noresults(empty_results_keywords):
    with raises(ValueError):
        [_ for _ in search_web(*empty_results_keywords)]


def test_quantity(google_results):
    assert len(google_results) == 10


def test_extraction(url):
    assert len(list(extract_nested_urls(url))) > 0


def test_recursive_0(url):
    result = recursive_extract_urls(url, level=0)
    assert len(list(result)) == 1


def test_resursive_1(url):
    recursive1 = list(recursive_extract_urls(url, level=1))
    non_recursive = list(extract_nested_urls(url))
    assert recursive1 == non_recursive


# take to much time
# def test_recursive_2(url):
#    recursive1 = list(recursive_extract_urls(url, level=1))
#    recursive2 = list(recursive_extract_urls(url, level=2))
#    assert len(recursive1) < len(recursive2)
