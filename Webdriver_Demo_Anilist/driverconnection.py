from selenium import webdriver

driver = webdriver.Chrome()

def connectToAnilist():
    driver.get("https://anilist.co/search/anime?sort=START_DATE_DESC")
