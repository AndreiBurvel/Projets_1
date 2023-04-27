import requests
from bs4 import BeautifulSoup

#Указываем ссылку для сбора информации.
url='https://www.hltv.org/results'

#Отсылаем запрос на страницу.
link=requests.get(url)

#Парсим наш ответ.
soup=BeautifulSoup(link.text, 'html.parser')

#Ищем информацию нужную нам.
find_day=soup.find('div', class_='results-holder allres')
find_today=find_day.find('div', class_='results-sublist')
all_matches=find_today.findAll('div', class_='result-con')
for i in range(len(all_matches)):
    team_one=all_matches[i].find('div', class_='line-align team1').text.strip()
    team_two=all_matches[i].find('div', class_='line-align team2').text.strip()
    score=all_matches[i].find('td', class_='result-score').text.strip()
    event=all_matches[i].find('span', class_='event-name').text.strip()
    print(f'{team_one} {score} {team_two} {event}')
