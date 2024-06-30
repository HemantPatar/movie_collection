import streamlit as st
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Function to get movie collections
def fetch_movie_data(movie_names, date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    day_of_week = date_obj.strftime("%A").lower()

    options = Options()
    options.add_argument("--window-size=1920,1200")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    results = {}

    for movie in movie_names:
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        try:
            try:
                search_query = f"{movie} movie {date} {day_of_week} collection"
                url = f"https://www.google.com/search?q={search_query}"
                # print(url)
                driver.get(url)
                time.sleep(3)
                result_element = driver.find_element(by=By.XPATH,
                                          value='//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div//b')
            except:
                search_query = f"{movie} movie {date} collection"
                url = f"https://www.google.com/search?q={search_query}"
                # print(url)
                driver.get(url)
                time.sleep(3)
                result_element = driver.find_element(by=By.XPATH,
                                          value='//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div//b')
            results[movie] = result_element.text
        except:
            result_element1 = "From code not possible try manually"
            results[movie] = result_element1
            # pass


        driver.quit()

    return results

# Streamlit app
def main():
    st.title("Movie Box Office Collection Finder")

    # Inputs for movie names and date
    movie_names = st.text_input("Enter movie names (comma-separated):")
    date = st.date_input("Select a date:", value=datetime.now()).strftime("%Y-%m-%d")

    if st.button("Fetch Data"):
        if movie_names:
            movie_list = [name.strip() for name in movie_names.split(",")]
            results = fetch_movie_data(movie_list, date)

            st.subheader("Results:")
            for movie, result in results.items():
                st.write(f"**{movie}**: {result}")
        else:
            st.warning("Please enter at least one movie name.")

if __name__ == "__main__":
    main()
