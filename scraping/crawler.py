import requests
from bs4 import BeautifulSoup
import time


def getHtml(base_url, directory=''):
    url = base_url + directory
    response = requests.get(url, timeout=5)
    if response.status_code != 200:
        print("Bad response code ", response.status_code, " when getting " , url)
        return False
    html = response.content
    page = BeautifulSoup(html, features="html.parser")
    return page


def getRacketUrls(catalog_page):
    racquet_links = catalog_page.findAll('a', attrs={'class': 'name'})
    racquet_urls = []
    for name in racquet_links:
        url = name['href']
        if(url.split('/')[-1].startswith('descpage')):
            racquet_urls.append(url)
    return racquet_urls


def findReviewDirectory(racquet_page):
    review_links = racquet_page.find('ul', attrs={'class': 'review_links'})
    for review_link in review_links.findAll('a', href=True):
        if(review_link.text == 'TW Reviews'):
            review_directory = review_link['href']
            return review_directory
