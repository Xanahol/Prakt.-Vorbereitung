from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import driverconnection as DC
from driverconnection import driver as Driver
import dbconnection as DBC
import malcook as Cook


def goToNextPage():
    element = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@class='link-blue-box next']")))
    Driver.get(element.get_attribute("href"))


def getAnimeInOrder():
    counter = 1

    while True:
        if counter <= 50:
            print("\nThe element Nr. {} has been selected.".format(counter))

            element = WebDriverWait(Driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "//table[@class='top-ranking-table']/tbody/tr[@class='ranking-list'][{}]/td[@class='title al va-t word-break']/a".format(counter))))

            newUrl = element.get_attribute("href")
            Driver.get(newUrl)

            WebDriverWait(Driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//tr")))

            Cook.insertAnimeInDB(getEnglishName(), getJapaneseName(), getType(
            ), getEpisodes(), getStatus(), getStudios(), getGenres(), getSynopsis())
            Driver.back()
            counter += 1
        elif counter > 50:
            goToNextPage()
            counter = 1


def getEnglishName():
    englishName = DC.getTextOfElement("//span[text()='English:']/..")

    try:
        return englishName[9:]
    except:
        return None


def getJapaneseName():
    japaneseName = DC.getTextOfElement("//span[text()='Japanese:']/..")

    try:
        return japaneseName[10:]
    except:
        return None


def getType():
    type = DC.getTextOfElement("//span[text()='Type:']/..")

    try:
        return type[6:]
    except:
        return None


def getEpisodes():
    episodes = DC.getTextOfElement("//span[text()='Episodes:']/..")

    try:
        if episodes[10:] != 'Unknown':
            return episodes[10:]
        else:
            return None
    except:
        return None


def getStatus():
    status = DC.getTextOfElement("//span[text()='Status:']/..")

    try:
        return status[8:]
    except:
        return None


def getStudios():
    studios = DC.getTextOfElement("//span[text()='Studios:']/..")

    try:
        return studios[9:]
    except:
        return None


def getGenres():
    genres = WebDriverWait(Driver, 10).until(EC.presence_of_all_elements_located(
        (By.XPATH, "//span[@itemprop='genre']/../a")))
    seperator = ', '
    genre = seperator.join([elem.text for elem in genres])
    return genre


def getSynopsis():
    synopsis = DC.getTextOfElement("//span[@itemprop='description']")

    try:
        synCut = synopsis[10:]
        return synCut[:-24]
    except:
        return None
