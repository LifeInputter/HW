# Автоматизация скачивания изображений:
# Библиотеки: BeautifulSoup, requests
# Описание: Скрипт для автоматического скачивания изображений с заданного сайта на основе определенных критериев
# (размер, формат и т.д.).


import os
import urllib.request
import requests
from bs4 import BeautifulSoup

url = 'https://www.onlinetours.ru/'
r = requests.get(url)

print(r.status_code)  # возвращает код запроса
print(r.content)  # вывод содержимого запроса в консоль
soup = BeautifulSoup(r.content, "html.parser")
image_tags = soup.find_all('img')

new_dir = "ImgWeb1"
parent_dir = r'C:\Users\Annam\Documents\PhytonProjectsUrban'
path = os.path.join(parent_dir, new_dir)
os.mkdir(path)
for tag in image_tags:
    image_url = tag["src"]
    filename = new_dir + url.split('/')[-1]
    try:
        urllib.request.urlretrieve(image_url, filename)
    except Exception as e:
        print(f'Невозможно загрузить {image_url} : {e}')
