import requests
from bs4 import BeautifulSoup

url = 'https://techgym.jp/?cat=2'

response = requests.get(url)

a = BeautifulSoup(response.text,'lxml')
article = a.find_all('li')
article_2 = a.find_all('div',class_ = 'vk_post')
print(article_2)
