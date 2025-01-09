import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import json
load_dotenv()

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/',headers=headers)
 
soup = BeautifulSoup(data.text, 'html.parser')

setTop50 = soup.select("#lst50 > td > div")
file_path = "melon_chart_50.txt"

rankArray = []
titleArray = []
artistArray = []
saveData = []
for i in setTop50 :
    rank = i.select_one("#lst50 > td:nth-child(2) > div > span.rank")
    if(rank is not None):
        rankArray.append(rank.text)

    title = i.select_one("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a")
    if(title is not None):
        titleArray.append(title.text)

    artist = i.select_one("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a")
    if(artist is not None):
        artistArray.append(artist.text)

for j, k, n in zip(rankArray, titleArray, artistArray):
    saveData.append({ "rank" : j, "title" : k, "artist" : n })

with open(f"{os.environ.get('DOWNLOAD_PATH')}{file_path}", "w") as file:
    file.write(json.dumps(saveData, indent=4, ensure_ascii=False))






        



