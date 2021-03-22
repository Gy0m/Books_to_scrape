import requests
import ipdb
import pandas as pd
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
        links.append('http://books.toscrape.com/' + link)  #récupère les liens des images
    print(len(links))              #compte le nombre de liens

with open('urls.csv', 'w') as file:
    for link in links:
        file.write(link + '\n')     #copie les liens dans un fichier csv et retour à la ligne

with open('urls.csv', 'r') as file:
    with open('product_information.csv', 'w') as outf:
        outf.write('intitulé,informations\n')
        for row in file:

            url = row.strip()
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.text, 'lxml')
                title = soup.find('div', {'class': 'product_main'}).find('h1')      #récupère les titres des livres
                data_table = soup.find('table', {'class': 'table table-striped'})   #identifie la classe du tableau
                data_table_ths = data_table('th')                                   #crée une variable avec les infos de th
                data_table_tds = data_table.find_all('td')                          #crée une variable avec les infos de td
                print('Titre: ' + title.text)                                       #écris dans le terminal "titre: + les infos des titres de livre

                ths = []

                for i, th in enumerate(data_table_ths):                             #itère les informations du tableau th
                    ths.append(th.text)                                             #les ajoutes à la liste th

                tds = []

                for i, td in enumerate(data_table_tds):
                    tds.append(td.text)

                df_productInformation = pd.DataFrame(data={'intitulé': ths, 'informations': tds})
                print(df_productInformation)

                #outf.write(title.text + ',' + th.text + ',' + td.text + '\n')
df_productInformation.to_csv('./product_information.csv', encoding='utf-8', index=False)