from datetime import datetime
import requests
import csv
import bs4

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

REQUEST_HEADER = {
    'User-Agent':USER_AGENT,
    'Accept-Language':'en-US, en;q=0.5'
}


def get_page_html(url):
    res = requests.get(url=url, headers = REQUEST_HEADER)
    return res.content

def extract_product_info(url):
    product_info = {}
    print(f'Scraping URL: {url}')
    html = get_page_html(url=url)
    print(html)


if __name__ == '__main__':
    print("Hello G.O.A.T")
    with open(r'C:\Users\Harish Paramathma\git\Mastering_BS4_Selenium\HTML_Scraper\amazon_product_urls.csv', newline = '') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            print(extract_product_info(url))