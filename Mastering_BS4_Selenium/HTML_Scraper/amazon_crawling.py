from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import csv
import json
from lxml.html import fromstring

user_input = input("Enter the product name to search: ").lower()
user_input = user_input.replace(' ','+')

pageno = 1
if pageno >= 2:
    url = f"https://www.amazon.in/s?k={user_input}&page={pageno}&ref=sr_pg_{pageno}"
else:
    url = f'https://www.amazon.in/s?k={user_input}'


headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'Accept-Encoding': 'gzip, deflate, br, zstd',
  'Accept': '*/*',
  'Upgrade-Insecure-Requests': '1',
}
proxy = ''
response = requests.request("GET", url, headers=headers)

# print(response.text)
soup1 = BeautifulSoup(response.content, 'html.parser')

"""
Our goal is to Extract:
Product Price   : ,
Product Title   : ,
Product Rating  : ,
Product Details : 
Finally write all the data into csv using pandas=> pd.to_csv()

"""
# print(soup.text)

searches = soup1.find_all('div', class_='puisg-col puisg-col-4-of-12 puisg-col-8-of-16 puisg-col-12-of-20 puisg-col-12-of-24 puis-list-col-right')

for search in searches:
    spans = search.find_all('span')
    fields = {}
    fields['Description'] = spans[0].text.strip()
    fields['Rating'] = spans[1].text.strip()
    fields['Rating_Overall'] = spans[5].text.strip()
    fields['Offered_Price'] = spans[7].text.strip()
    fields['Original_Price'] = spans[14].text.strip()
    fields['Save_Percentage'] = spans[16].text.strip()
    # fields['DeliveryDate'] = datetime.strptime(spans[22], '%d '


def find_div_with_text(soup, keywords):
    for div in soup.find_all('div'):
        if div.get_text(strip=True):
            for keyword in keywords:
                if keyword.lower() in div.get_text(strip=True).lower():
                    return div.get_text(strip=True)
    return None

keyword = ['GB','Storage','ROM']

fields = {}
for search in searches:
    fields['link'] = 'https://www.amazon.in' +search.find('a').get('href')


soup = fromstring(response.content)
search_elements = soup.xpath("//div[contains(@class,'a-section a-spacing-small a-spacing-top-small')]")
print(search_elements)




