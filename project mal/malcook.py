from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from driverconnection import driver as Driver
import dbconnection as DBC

cur = DBC.cur
conn = DBC.conn


def insertAnimeInDB(englishName, japaneseName, type, episodes, status, studios, genres, synopsis):
    sql = """
    INSERT INTO anime("englishName", "japaneseName", type, episodes, status, studios, genres, synopsis)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"""
    cur.execute(sql, (englishName, japaneseName, type,
                      episodes, status, studios, genres, synopsis))
    conn.commit()


def resetDB():
    sql = """
    ALTER SEQUENCE anime_id_seq RESTART WITH 1;
    DELETE FROM anime;"""
    cur.execute(sql)
    conn.commit()
