import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/index.html'

response = requests.get(url)

if response.ok:
    links = []
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.findAll('div', class_="image_container")
    for div in divs:
        a = div.find('a')
        link = a['href']
        links.append('http://books.toscrape.com/' + link)  # récupère les liens des images
    print(len(links))  # compte le nombre de liens

with open('urls.csv', 'w') as file:
    for link in links:
        file.write(link + '\n')  # copie les liens dans un fichier csv et retour à la ligne

with open('urls.csv', 'r') as file:

    for url in file:

        url = url.strip()
        response = requests.get(url)
        if response.ok:
            def scrape():
                soup = BeautifulSoup(response.text, 'lxml')
                title = soup.find('div', {'class': 'product_main'}).find('h1')  # récupère les titres des livres
                stars = soup.find('div', {'class': 'star-rating'})
                data_table = soup.find('table', {'class': 'table table-striped'})  # identifie la classe du tableau
                data_table_ths = data_table('th')  # crée une variable avec les infos de th
                data_table_tds = data_table.find_all('td')  # crée une variable avec les infos de td



                ths = []

                for i, th in enumerate(data_table_ths):  # itère les informations du tableau th
                    ths.append(th.text)  # les ajoutes au dict ths

                tds = []

                for i, td in enumerate(data_table_tds):
                    tds.append(td.text)

                    csv_columns = ['Titre', 'Intitulé', 'Informations']
                    dict = [
                        {'Titre': title.text, 'Intitulé': ths, 'Informations': tds}
                    ]
                    #print(dict)
                    csv_file = "product_information.csv"
                    with open(csv_file, 'w', newline='') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                        writer.writeheader()
                        for data in dict:
                            writer.writerow(data)
print(scrape())
