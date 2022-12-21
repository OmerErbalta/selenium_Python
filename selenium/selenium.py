import time
import pytesseract
import cv as cv
from selenium import webdriver
from selenium.webdriver.common.by import By
"Path = chromedriver.exe location"
Path = "//Users/omererbalta//Downloads//chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.get("https://github.com")
driver.find_element(
    By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]").send_keys("OmerErbalta")
time.sleep(1)
driver.find_element(
    By.XPATH, '//*[@id="jump-to-suggestion-search-global"]/a/div[3]/span[2]').click()
time.sleep(1)
driver.find_element(
    By.XPATH, '/html/body/div[1]/div[4]/main/div/div[2]/nav[1]/a[10]').click()
time.sleep(1)
driver.find_element(
    By.XPATH, '//*[@id="user_search_results"]/div/div/div[2]/div[1]/div[1]/a[1]').click()
time.sleep(1)
driver.find_element(
    By.XPATH, '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/div/span/span/a').click()
time.sleep(10)
