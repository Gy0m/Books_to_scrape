import requests
from bs4 import BeautifulSoup
import csv


def get_books_urls():
    links = []
    # for i in range(51):
    # url = 'http://books.toscrape.com/catalogue/page-' + str(i) + '.html'
    url = 'http://books.toscrape.com/index.html'

    response = requests.get(url)
    if response.ok:
        # print('Page: ' + str(i))
        # links = []
        soup = BeautifulSoup(response.text, 'lxml')
        divs = soup.findAll('div', class_="image_container")
        for div in divs:
            a = div.find('a')
            link = a['href']
            links.append('http://books.toscrape.com/' + link)  # récupère les liens des images
    print(links)  # compte le nombre de liens
    return links


def to_integer(string_value):
    integer_value = None
    if string_value == 'One':
        integer_value = '1'
    if string_value == 'Two':
        integer_value = '2'
    if string_value == 'Tree':
        integer_value = '3'
    if string_value == 'Four':
        integer_value = '4'
    if string_value == 'Five':
        integer_value = '5'
    return integer_value


def get_book_info(url):
    response = requests.get(url)
    if not response.ok:
        return

    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('div', {'class': 'product_main'}).find('h1')  # récupère les titres des livres
    star = soup.find('p', {'class': 'star-rating'}).get('class')
    stars = to_integer(star[-1])
    categorys = soup.find('ul', {'class': 'breadcrumb'}).find_all_next('a', limit=3)
    category = categorys[-1]
    image_url = soup.find('div', {'class': 'item'}).find('img').get('src')
    product_description = soup.find('div', {'id': 'product_description'}).find_next('p')
    table = soup.find('table', {'class': 'table table-striped'})
    table_trs = table('tr')
    trs = []
    for tr in table_trs:
        trs.append(tr.text)

        print(tr.find('th').text)
        tr.find('td')

    return {
        'product_page_url': url,
        'title': title,
        'stars': stars,
        'category': category,
        'image_url': image_url,
        'product_description': product_description,
    }


for url in get_books_urls():

    url = url.strip()


csv_file = "product_information.csv"
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=get_book_info(url))
    writer.writeheader()
    for data in get_book_info(url):
        writer.writerow(data)


# for category in categories:
#     with open('product_information.csv', 'r') as books:  #ouvrir le fichier csv
# for books in get_books(url_books):
#  #ecrire dans le csv
