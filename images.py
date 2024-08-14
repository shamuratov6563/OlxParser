from bs4 import BeautifulSoup
import requests
from os.path  import basename

r = requests.get("https://scrapingclub.com/exercise/list_basic/?page=1")
soup = BeautifulSoup(r.content, "lxml")


images = soup.find_all('img', class_ ='card-img-top img-fluid')

for image in images:
    with open(basename(image['src']), "wb") as f:
        f.write(requests.get("https://scrapingclub.com" + image['src']).content)