from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
url = 'https://www.python.org'


driver = webdriver.Chrome()
driver.get(url)

emaildd = driver.find_element(by=By.NAME, value='q')

button = driver.find_element(by=By.CSS_SELECTOR, value='button')

emaildd.send_keys('functions')
button.click()
print(driver.title)
time.sleep(20)


