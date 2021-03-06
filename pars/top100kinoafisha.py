import requests
from bs4 import BeautifulSoup
import fake_useragent


user = fake_useragent.UserAgent().random
header = {'user-agent': user}
# top rating
link = "https://www.kinoafisha.info/rating/movies/"
responce = requests.get(link, headers=header).text
soup = BeautifulSoup(responce, 'html.parser')
block_title = soup.find_all('a', class_='movieItem_title')
block_genre = soup.find_all('span', class_='movieItem_genres')
block_picture = soup.find_all('img', class_='picture_image')
index_of_toplist = 1
print('ТОП 100')
for title, genres, pictures in zip(block_title, block_genre , block_picture):
    print(index_of_toplist, title.findAll(text=True))
    print(genres.findAll(text=True))
    print(pictures)
    index_of_toplist = index_of_toplist + 1


print(header)
