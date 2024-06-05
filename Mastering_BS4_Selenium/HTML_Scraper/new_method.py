import requests
from lxml.html import fromstring

# URL to scrape
url = 'https://quotes.toscrape.com/'

# Perform the GET request
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# Parse the HTML content
soup = fromstring(response.content)

# Select elements using XPath
anchor_elements = soup.xpath('//a')  # Replace with your XPath expression

# Iterate over the selected elements and print their href attributes
for anchor in anchor_elements:
    href = anchor.get('href')
    if href:  # Ensure the href attribute exists
        print(href)

print('success')