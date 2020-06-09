from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from driverconnection import driver as Driver


def saveHTML():
    with open("Prakt.-Vorbereitung/Webdriver_Demo_Anilist/HTML_Sources/page_source.html", "w") as f:
        f.write(Driver.page_source)


# Scrollt zum Ende der Seite zwischen 5 und 12 mal
def scrollDownRandomly():
    ran = round(random.uniform(5, 12))
    for _ in range(ran):
        last_height = Driver.execute_script(
            "return document.body.scrollHeight")

        Driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(1)

        new_height = Driver.execute_script("return document.body.scrollHeight")

        last_height = new_height


def scrollDownOnce():
    last_height = Driver.execute_script("return document.body.scrollHeight")

    Driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)

    new_height = Driver.execute_script("return document.body.scrollHeight")

    last_height = new_height


# Holt sich einen von 100 Animeeinträgen und liest den Namen aus
def getRandomNames():
    while True:
        scrollDownRandomly()

        ran = round(random.uniform(0, 100))
        print("\nThe element Nr. {} has been selected.".format(ran))
        print("The name of the Anime is:")

        element = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='results cover']/div[{}]/a[1]".format(ran))))
        newUrl = element.get_attribute("href")
        Driver.get(newUrl)

        elementOnPage = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='data']/div[last()-1]/div[@class='value']")))
        print(elementOnPage.text)
        Driver.back()


def getNamesInOrder():
    counter = 1

    while True:

        print("\nThe element Nr. {} has been selected.".format(counter))
        print("The name of the Anime is:")

        try:
            element = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='results cover']/div[{}]/a[1]".format(counter))))
        except:
            scrollDownOnce()
            element = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//div[@class='results cover']/div[{}]/a[1]".format(counter))))

        newUrl = element.get_attribute("href")
        Driver.get(newUrl)

        elementOnPage = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='data']/div[last()-1]/div[@class='value']")))
        print(elementOnPage.text)
        Driver.back()
        scrollDownOnce()
        counter += 1
