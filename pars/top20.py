import fake_useragent
import requests
from bs4 import BeautifulSoup
import fake_useragent


user = fake_useragent.UserAgent().random
header = {'user-agent': user}
link = "https://zen.yandex.ru/media/inrating/top20-luchshih-novyh-filmov-2021-vyshedshih-v-horoshem-kachestve-na-dannyi-moment-605980704c239f13cdb4ed80"
responce = requests.get(link, headers=header).text
soup = BeautifulSoup(responce, 'html.parser')
block_title_website = soup.find('h1', class_="article__title").text
block_title_films = soup.find_all('h2')
for name in block_title_films:
    print(name.findAll(text=True))

print(block_title_website)
#print(soup.prettify())
print(header)
