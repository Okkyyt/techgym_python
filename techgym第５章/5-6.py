import requests
from bs4 import BeautifulSoup

url = 'https://techgym.jp/?cat=2'

response = requests.get(url)

a = BeautifulSoup(response.text,'lxml')
article = a.find_all('li')
article = a.find_all('div',class_ = 'vk_post')

for i in article:
    titles = i.find_all('h5')[0].getText()

    print(titles)