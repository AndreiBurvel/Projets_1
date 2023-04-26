import requests
from bs4 import BeautifulSoup

#Указываем URL страницы который нам надо распарсить.
url='https://www.hltv.org/ranking/teams'

#Отправляем запрос на данный URL.
link=requests.get(url)

#Парсим ответ от страницы по нашему запросу.
soup=BeautifulSoup(link.text, 'html.parser')

#Ищем дату рейтинга.
date=soup.find('div', class_='regional-ranking-header').text.strip()

#Находим класс который обединяет все команды и ищем их все.
all_find=soup.findAll('div', class_='ranked-team standard-box')

#Выводим дату.
print(date)

#Проходим циклом по всем тегам и ищем нужные нам данне (комманда и количество очков).
for i in range(0, len(all_find)):
    team=all_find[i].find('span', class_='name').text
    points=all_find[i].find('span', class_='points').text.replace(')','')
    points=points.replace('(','')
    print(f'{i+1}. {team} - {points}')