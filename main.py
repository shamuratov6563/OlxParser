import requests
from bs4 import BeautifulSoup

for i in range(1, 4):
    url = f'https://scrapingclub.com/exercise/list_basic/?page={i}'

    response = requests.get(url)

    # print(response.text)

    soup = BeautifulSoup(response.text, 'lxml')

    quotes = soup.find_all('div', class_='w-full rounded border')

    for i in quotes:
        title = i.find('h4')
        price = i.find('h5')
        print(title.text, price.text)