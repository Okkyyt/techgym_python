import requests
from bs4 import BeautifulSoup

url = 'https://news.yahoo.co.jp/'

texts = requests.get(url)

soup = BeautifulSoup(texts.text,'lxml')

article = soup.find_all('li')
print(article)

article = soup.find_all('li',class_ = 'topicsListltem')
print(article)
