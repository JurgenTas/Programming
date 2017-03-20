# coding=utf-8
__author__ = 'J Tas'

import requests
from bs4 import BeautifulSoup


def make_soup(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")  # use python html parser
    return soup


def main():
    url = "http://www.nu.nl"
    soup = make_soup(url)

    # get class type:
    print(type(soup))

    # get nested data structure:
    print(soup.prettify())

    # extracting all the URLs found within a page’s < a > tags:
    for link in soup.find_all('a'):
        print(link.get('href'))


if __name__ == "__main__":
    main()
