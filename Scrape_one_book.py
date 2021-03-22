import requests
import ipdb
import pandas as pd
from bs4 import BeautifulSoup

'''

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

with open('urls.csv', 'r') as file:
    for row in file:
        url = row.strip()
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')
            upc = soup.find()
            
        '''

url = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('div', {'class': 'product_main'}).find('h1')
    data_table = soup.find('table', {'class': 'table table-striped'})
    data_table_ths =data_table('th')
    data_table_tds = data_table.find_all('td')
    print('Titre: ' + title.text )


ths = []

for i, th in enumerate(data_table_ths):
    ths.append(th.text)

tds = []

for i, td in enumerate(data_table_tds):
    tds.append(td.text)

df_productInformation = pd.DataFrame(data={'intitulé': ths, 'informations': tds})
print(df_productInformation)

df_productInformation.to_csv('./output.csv', encoding='utf-8', index=False)