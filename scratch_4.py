import requests,time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
movie_names = ["Kalki", "A quiet place: day one"]
date = "2024-06-27"
from datetime import datetime
date_obj = datetime.strptime(date, "%Y-%m-%d")
day_of_week = date_obj.strftime("%A").lower()
options = Options()
for movie in movie_names:
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    try:
        find = f"{movie} movie {date} {day_of_week} collection"
        url = f"https://www.google.com/search?q={find}"
        print(url)
        driver.get(url)
        time.sleep(3)
        abc = driver.find_element(by=By.XPATH,
                                  value='//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div//b')
    except:
        find = f"{movie} movie {date} collection"
        url = f"https://www.google.com/search?q={find}"
        print(url)
        driver.get(url)
        time.sleep(3)
        abc = driver.find_element(by=By.XPATH,
                                  value='//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div//b')

    # try:
    #     abc = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/span/span/b')
    #
    # except:
    #     abc = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/span[1]/span/span/span/b')
    print(movie)
    print(abc.text)
    driver.quit()