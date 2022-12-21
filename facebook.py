from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
url = 'https://web.facebook.com/?_rdc=1&_rdr'

driver.get(url)

driver.implicitly_wait(10)
user_name = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
submit = driver.find_element(By.NAME, value='login')

user_name.send_keys(os.environ.get('EMAIL'))
password.send_keys(os.environ.get('PASSWORD'))
submit.click()

time.sleep(30)
