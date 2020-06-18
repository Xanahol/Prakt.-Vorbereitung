from selenium import webdriver

driver = webdriver.Chrome()


def connectToMyAnimelist():
    driver.get("https://myanimelist.net/topanime.php?limit=0")


def getTextOfElement(xpath):
    try:
        return driver.find_element_by_xpath(xpath).text
    except:
        return None
