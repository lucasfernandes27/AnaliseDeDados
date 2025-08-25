#
import pandas
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.google.com/')
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])

print("Pandas: ")
url_dados = pandas.read_html(url='https://www.google.com/')
print(url_dados[0].head(10))