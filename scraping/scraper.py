import requests
from bs4 import BeautifulSoup
import time


def getRacquetSpecsDict(racquet_page):
    table = racquet_page.find('div', attrs={'class': 'rac_specs'}).table
    # tbody tag is sometimes added
    if table.find('tbody'):
        table = table.tbody
        
    racquet_specs = {}
    for row in table.findAll('tr', recursive=False):
        key = row.td.find('strong')
        key_text = key.text.strip(' :')

        value = key.next_sibling
        # skip <br> tags to find the next sibling
        while(value.name == 'br'):
            value = value.next_sibling

        if(value.name == 'table'):
            value_text = value.find('td').text
        else:
            value_text = value.strip(' /')

        racquet_specs[key_text] = value_text
    return racquet_specs


def getRacquetName(racquet_page):
    racquet_name = racquet_page.find('h1', attrs={'class': 'name'})
    return racquet_name.text


def getReviewDate(review_page):
    footer = review_page.find('div', attrs={'class': 'review_footer'}).p
    review_date_sentence = footer.text.split('.')[0]
    review_date_str = review_date_sentence.split(':')[1].strip()
    
    review_date = time.strptime(review_date_str, '%B %Y')
    return review_date

