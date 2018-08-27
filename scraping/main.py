import click
import crawler
import scraper


def main():
    index_url = 'https://www.tennis-warehouse.com'
    catalog_directory = '/Headracquets.html'
    catalog_page = crawler.getHtml(index_url, catalog_directory)
    urls = crawler.getRacketUrls(catalog_page)
    return urls


if __name__ == '__main__':
    print(main())
