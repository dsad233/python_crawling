import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://vibe.naver.com/chart/domestic/',headers=headers)
 
soup = BeautifulSoup(data.text, 'html.parser')

bestMusicList = soup.find("body")

print(bestMusicList)
# for i in bestMusicList:
#     # title = i.select("td.song > div.title_badge_wrap > span > a")
#     print(bestMusicList)

#     if(len(bestMusicList) == 100):
#         break

