from selenium import webdriver

driver = webdriver.Chrome()


def connectToMyAnimelist():
    driver.get("https://myanimelist.net/topanime.php?limit=0")


def saveHTML(name):
    with open("Prakt.-Vorbereitung/project/html_sources/page_source_{}.html".format(name), "w") as f:
        f.write(Driver.page_source)
