import requests
from bs4 import BeautifulSoup
import sqlite3
from create_db import CreateDb

CreateDb()

url = 'https://balun.com.ua/ua/g95153041-hlopavki'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

name = soup.find_all('a', class_='b-product-gallery__title')
price = soup.find_all('div', class_='b-product-gallery__prices')
availability = soup.find_all('span', class_='b-product-gallery__state b-product-gallery__state_val_avail')
data = {}

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
SQL = '''INSERT INTO balun (Name, Price, Availability)
VALUES (?,?,?)'''


for _ in range(len(name)):
    cursor.execute(SQL, [name[_].text, price[_].text, availability[_].text])

conn.commit()
conn.close()

for _ in range(len(name)):
    data[price[_].text] = {name[_].text:availability[_].text.split()[1:]}