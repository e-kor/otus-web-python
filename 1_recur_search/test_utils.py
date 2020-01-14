import requests
from pytest import fixture, raises

from utils import extract_nested_urls, recursive_extract_urls, search_web


class TestSearch:
    """
    testing of search results with different inputs
    """

    def test_emoty_input(self):
        with raises(ValueError):
            [_ for _ in search_web()]

    def test_noresults(self, empty_results_keywords):
        with raises(ValueError):
            [_ for _ in search_web(*empty_results_keywords)]

    def test_regular_quantity(self, google_results):
        assert len(google_results) == 10


class TestUrlExtraction:
    """
    testing functions for extraction of url from web pages
    """

    def test_extraction(self, url):
        assert len(list(extract_nested_urls(url))) > 0

    def test_broken_url_extraction(self, broken_url):
        with raises(requests.exceptions.InvalidSchema):
            list(extract_nested_urls(broken_url))

    def test_recursive_0(self, url):
        result = recursive_extract_urls(url, level=0)
        assert len(list(result)) == 1

    def test_resursive_1(self, url):
        recursive1 = list(recursive_extract_urls(url, level=1))
        non_recursive = list(extract_nested_urls(url))
        assert recursive1 == non_recursive


# def test_recursive_2(url):
#    recursive1 = list(recursive_extract_urls(url, level=1))
#    recursive2 = list(recursive_extract_urls(url, level=2))
#    assert len(recursive1) < len(recursive2)
