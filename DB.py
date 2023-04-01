import sqlite3
from bs4 import BeautifulSoup
import datetime
import requests

response = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%87%D0%B5%D1%80%D0%BD%D0%B8%D0%B3%D0%BE%D0%B2')
resp_text = response.text

date_now = datetime.datetime.now()

soup = BeautifulSoup(resp_text, features= 'html.parser')
soup_l = soup.find_all('p', {'class': 'today-temp'})

res = soup_l[0].text

connection = sqlite3.connect('itstepDB.sl3', 5)

cur = connection.cursor()
cur.execute(f'INSEART INTO weather (date,temp) VALUES ("{date_now}", "{res}");')

connection.commit()
connection.close()