from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from driverconnection_mal import driver as Driver


def goToNextPage():
    element = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//a[@class='link-blue-box next']")))
    Driver.get(element.get_attribute("href"))


def getNamesInOrder():
    counter = 1

    while True:
        try:
            if counter <= 50:
                print("\nThe element Nr. {} has been selected.".format(counter))
                print("The name of the Anime is:")

                element = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//table[@class='top-ranking-table']/tbody/tr[@class='ranking-list'][{}]/td[@class='title al va-t word-break']/a".format(counter))))

                newUrl = element.get_attribute("href")
                Driver.get(newUrl)

                elementOnPage = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//td[@class='borderClass']/div/div[6]")))
                print(elementOnPage.text)
                Driver.back()
                counter += 1
            elif counter > 50:
                goToNextPage()
                counter = 1
        except:
            pass
