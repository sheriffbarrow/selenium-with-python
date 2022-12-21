from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pickle


def demo():
    url = 'https://www.moneyhelper.org.uk/en#'

    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    cookies = driver.get_cookies()
    pickle.dump(cookies, open('cookies.pkl', 'wb'))

    time.sleep(20)


demo()
