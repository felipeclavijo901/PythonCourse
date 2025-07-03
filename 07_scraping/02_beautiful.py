from bs4 import BeautifulSoup
import requests

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'
response = requests.get(url)

if response.status_code == 200:
    print("La consulta fue exitosa.")
    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.title
    if title_tag:
        print(title_tag.string)
    # print(soup)