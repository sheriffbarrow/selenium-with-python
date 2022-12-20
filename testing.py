from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = 'https://www.python.org'

def demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    cookie = driver.get_cookies()
    print( driver.get_cookies())

    emaildd = driver.find_element(by=By.NAME, value='q')

    button = driver.find_element(by=By.CSS_SELECTOR, value='button')

    emaildd.send_keys('functions')
    button.click()
    print(driver.title)

    time.sleep(20)


