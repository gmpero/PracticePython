import fake_useragent
import requests
from bs4 import BeautifulSoup
import fake_useragent


user = fake_useragent.UserAgent().random
header = {'user-agent': user}
link = "https://lichess.org/@/RusChessMaster"
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', {'class': 'angle-content'})
block_section = block.find('section')
title_section = block_section.find_all('time')[0].text
score_puzzle = block_section.find_all('div')[3].text
#print(block_section)
print(title_section)
print(score_puzzle)
#print(soup.prettify())
print(header)
