# selenium의 webdriver를 사용하기 위한 import
from selenium import webdriver

# selenium으로 키를 조작하기 위한 import
# from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
import json

driver = webdriver.Chrome()
driver.implicitly_wait(time_to_wait=10)


driver.get('https://vibe.naver.com/chart/domestic/')

rankArray = []
titleArray = []
saveArray = []
try :
    # search = driver.find_elements(By.CSS_SELECTOR, "#content > div.track_section > div:nth-child(2) > div > table > tbody")
    # for data in search:
    rank = driver.find_elements(By.CSS_SELECTOR, "#content > div.track_section > div:nth-child(2) > div > table > tbody > tr > td > span.text")
    for data in rank:
        if(data.text != ""):
            rankArray.append(data.text)

    title = driver.find_elements(By.CSS_SELECTOR, "#content > div.track_section > div:nth-child(2) > div > table > tbody > tr > td.song > div > span > a")
    for data in title:
        if(data.text != ""):
            titleArray.append(data.text)
    
    for j, k in zip(rankArray, titleArray):
        saveArray.append({ "rank" : j, "title" : k })

    

    print(json.dumps(saveArray, indent=4, ensure_ascii=False))
except Exception as err:
    print(err)
    print("에러 발생")
finally:
    driver.close()