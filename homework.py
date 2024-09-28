
import requests
from bs4 import BeautifulSoup
import json

url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Получаем количество страниц
pagination = soup.find('ul', class_='pager')
num_pages = int(pagination.find('li', class_='current').text.split()[-1])

books = []

for page in range(1, num_pages + 1):
    page_url = f'{url}catalogue/page-{page}.html'
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for book in soup.find_all('article', class_='product_pod'):
        title = book.find('h3').text
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text

        # Проверяем, если строка доступности находится в ожидаемом формате
        if '(' in availability and ')' in availability:
            availability = int(availability.split('(')[1].split(' ')[0])
        else:
            availability = 0  # или некоторое другое значение по умолчанию

        description_element = book.find('p', class_='')
        if description_element is not None:
            description = description_element.text
        else:
            description = ''  # или некоторое другое значение по умолчанию

        book_info = {
            'title': title,
            'price': price,
            'availability': availability,
            'description': description
        }
        books.append(book_info)

# Сохраняем информацию о книгах в JSON-файле
with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=4)

print('Информация о книгах сохранена в файле books.json')

