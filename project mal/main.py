#################################
#      Created by Noël B.       #
#    in preparation for the     #
#     1 year of internship      #
#           18.06.2020          #
#################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import driverconnection as DC
import malcook as Cook
import crawler as Crawler


Cook.resetDB()
DC.connectToMyAnimelist()
Crawler.getAnimeInOrder()
