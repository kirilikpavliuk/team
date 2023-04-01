from bs4 import BeautifulSoup
import requests

response = requests.get('https://coinmarketcap.com/')
response_text = response.text

if response.status_code == 200:
    soup = BeautifulSoup(response_text,
                         features='html.parser')
