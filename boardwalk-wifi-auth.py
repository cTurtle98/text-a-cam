'''

text-a-cam project

https://github.com/cTurtle98/text-a-cam

temporary
boardwalk wifi auth selenium script
waiting for Chris to finish the shell script

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

GETURL = 'https://www.google.com/'

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get(GETURL)

wait.until(EC.url_changes(GETURL))

button = browser.find_element_by_name("")

button.click()