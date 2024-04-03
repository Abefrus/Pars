import json
import requests
from bs4 import BeautifulSoup
import sqlite3
from create_db import CreateDb

CreateDb()


url = 'http://quotes.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')
data = {}

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
SQL = '''INSERT INTO quotes (author, quote, tags)
VALUES (?,?,?)'''
# print(quotes)
for _ in range(len(quotes)):
    print(quotes[_].text)
    print(authors[_].text)
    print(tags[_].text.split()[1:])
    tag = ', '.join(tags[_].text.split()[1:])
    cursor.execute(SQL, [quotes[_].text, authors[_].text, tag])
conn.commit()
conn.close()
for _ in range(len(quotes)):
    data[authors[_].text] = {quotes[_].text:tags[_].text.split()[1:]}

print(data)
with open('result.json', 'w',encoding='utf-8') as file:
    json.dump(data, file)


