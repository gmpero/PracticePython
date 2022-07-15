import requests
from bs4 import BeautifulSoup
import fake_useragent


user = fake_useragent.UserAgent().random
header = {'user-agent': user}
link = "https://www.kinoafisha.info/rating/movies/"
responce = requests.get(link, headers=header).text
soup = BeautifulSoup(responce, 'html.parser')
block_title_website = soup.find_all('a', class_='movieItem_title')
i = 1
for title in block_title_website:
    print(i, title.findAll(text=True))
    i+=1

#print(block_title_website)
#print(block_title_website)
#print(soup.prettify())
print(header)
