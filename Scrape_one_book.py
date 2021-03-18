import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/index.html'

response = requests.get(url)

if response.ok:
    links = []
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.findAll('div', class_="image_container")
    for div in divs:
        a = div.find('a')
        link = a['href']
        links.append('http://books.toscrape.com/' + link)
    print(len(links))

with open('urls.csv', 'w') as file:
    for link in links:
        file.write(link + '\n')
