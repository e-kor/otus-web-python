import argparse
from itertools import islice
from utils import search_web, extract_nested_urls, recursive_extract_urls


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'keywords', help='strings passed to google search', nargs='+')
    parser.add_argument('-l', '--limit', help='maximum count of urls to display', default=10 ** 3, type=int,
                        required=False)
    parser.add_argument('-r', '--recursion', help='level of recursion to search through pages', default=0, type=int,
                        required=False)
    args = parser.parse_args()

    search_results = search_web(*args.keywords)
    nested_urls = recursive_extract_urls(*search_results, level=args.recursion)

    for count, url in enumerate(islice(nested_urls, args.limit)):
        print(f"{count}\t{url}")
