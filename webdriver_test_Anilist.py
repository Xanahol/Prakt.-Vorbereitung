from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

driver = webdriver.Chrome()
driver.get("https://anilist.co/search/anime?sort=START_DATE_DESC")


# Scrollt zum Ende der Seite zwischen 5 und 12 mal
def scrollDown():
    ran = round(random.uniform(5, 12))
    for _ in range(ran):
        last_height = driver.execute_script(
            "return document.body.scrollHeight")

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(1)

        new_height = driver.execute_script("return document.body.scrollHeight")

        last_height = new_height


# Holt sich einen von 140 Animeeinträgen und liest den Namen aus
def getRandomNames():
    scrollDown()

    ran = round(random.uniform(0, 140))
    print("The element Nr. {} has been selected.".format(ran))
    print("The name of the Anime is:")

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='results cover']/div[{}]/a[1]".format(ran))))
    newUrl = element.get_attribute("href")
    driver.get(newUrl)

    elementOnPage = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='data']/div[last()-1]/div[@class='value']")))
    print(elementOnPage.text)
    print()
    driver.back()


# Loopt die Funktion
while True:
    getRandomNames()
