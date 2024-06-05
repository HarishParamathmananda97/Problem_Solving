import requests
from bs4 import BeautifulSoup

url = "https://www.collegesidekick.com/study-docs/3342991"

payload = ""
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'Accept-Encoding': 'gzip, deflate, br, zstd',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Upgrade-Insecure-Requests': '1',
  'Content-Type':'text/html'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


