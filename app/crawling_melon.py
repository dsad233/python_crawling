import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/',headers=headers)
 
soup = BeautifulSoup(data.text, 'html.parser')

setTop50 = soup.select("#lst50 > td > div")
file_path = "title.txt"

rankArray = []
titleArray = []
saveData = []
for i in setTop50 :
    rank = i.select_one("#lst50 > td:nth-child(2) > div > span.rank")

    # if rank is not None:
    #     print(rank.text, end="위\n")

    title = i.select_one("#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a")

    # if title is not None:
    #     print(title.text, "\n")
        

    if(rank is not None):
        rankArray.append(rank.text)

    if(title is not None):
        titleArray.append(title.text)

    if(len(setTop50) == 50):
        break


for j, k in zip(rankArray, titleArray):
    saveData.append({ "rank" : j, "title" : k })
    


print("saveData : ",saveData)
with open(f"/Users/mabook/Downloads/{file_path}", "w") as file:
    # file.write(json.dump(saveData))
    json.dump(saveData, file, indent=4, ensure_ascii=False)
    # file.write()






        



