import requests

url = "https://markets.newyorkfed.org/read?productCode=50&eventCodes=525&startDt=2020-03-02&endDt=2024-03-06&fields=averageIndex30days,averageIndex90days,averageIndex180days,sofrIndex,refRateDt&sort=postDt:1"

payload = {}
headers = {
  'Accept': 'application/json, text/plain, */*:',
  'Accept-Encoding': 'gzip, deflate, br, zstd:',
  'Accept-Language': 'en-US,en;q=0.9:',
  'Origin': 'https://www.newyorkfed.org',
  'Referer': 'https://www.newyorkfed.org/',
  'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
  'Sec-Ch-Ua-Mobile': '?0:',
  'Sec-Ch-Ua-Platform': '"Windows":',
  'Sec-Fetch-Dest': 'empty:',
  'Sec-Fetch-Mode': 'cors:',
  'Sec-Fetch-Site': 'same-site:',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36:',
 }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
