import click
import crawler
import scraper


def main():
    index_url = 'https://www.tennis-warehouse.com'
    catalog_directory = '/Headracquets.html'
    catalog_page = crawler.getHtml(index_url, catalog_directory)
    urls = crawler.getRacketUrls(catalog_page)

    racquet_specs = {}
    for url in urls:
        racquet_page = crawler.getHtml(url)
        try:
            racquet_name = scraper.getRacquetName(racquet_page)
            racquet_spec = scraper.getRacquetSpecsDict(racquet_page)
            racquet_specs[racquet_name] = racquet_spec
        except:
            print("Couldn't scrape ", url)

    return racquet_specs


if __name__ == '__main__':
    racquet_specs = main()
    print(racquet_specs)
    print(len(racquet_specs))
