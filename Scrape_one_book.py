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
    return links


def to_integer(string_value):
    integer_value = None
    if string_value == 'One':
        integer_value = '1'
    if string_value == 'Two':
        integer_value = '2'
    if string_value == 'Three':
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
    table_trs = table.find_all('tr')
    trs = []
    tds = []
    for tr in table_trs:
        trs.append(tr.text)

    data = {
        'product_page_url': url,
        'upc': trs[0],
        'title': title,
        'price_including_tax': trs[3],
        'price_excluding_tax': trs[2],
        'number_available': trs[5],
        'product_description': product_description,
        'category': category.text,
        'stars': stars,
        'image_url': image_url,
    }
    print(data)
    return data


csv_file = "product_information.csv"
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames={
        'product_page_url', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available',
        'product_description', 'category', 'stars', 'image_url',
    })
    writer.writeheader()
    for url in get_books_urls():
        url = url.strip()
        for data in get_book_info(url):
            writer.writerow(data)


# for category in categories:
#     with open('product_information.csv', 'r') as books:  #ouvrir le fichier csv
# for books in get_books(url_books):
#  #ecrire dans le csv
