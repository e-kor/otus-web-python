from .utils import search_web, extract_nested_urls, recursive_extract_urls
from pytest import fixture, raises


@fixture
def empty_results_keywords():
    return 'heldsajkhbdas sajhkdas'


@fixture
def google_results():
    return list(search_web('some keywords'))


def test_noresults(empty_results_keywords):
    with raises(ValueError):
        [_ for _ in search_web(*empty_results_keywords)]


def test_quantity(google_results):
    assert len(google_results) == 10


def test_extraction(google_results):
    assert len(list(extract_nested_urls(google_results[0]))) > 0


def test_recursive_0(google_results):
    result = recursive_extract_urls(google_results[0], level=0)
    assert len(list(result)) == 1


# def test_recursive_1(google_results):
#    result = recursive_extract_urls(google_results[0], level=1)
#    assert len(list(result)) > 1
