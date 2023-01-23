from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import pickle


url = 'https://web.facebook.com'


def login():

    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    driver.implicitly_wait(10)

    user_name = driver.find_element(By.XPATH, value='//*[@id="email"]')
    password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
    login = driver.find_element(By.NAME, value='login')

    user_name.send_keys(os.environ.get('EMAIL'))
    password.send_keys(os.environ.get('PASSWORD'))
    login.click()
    time.sleep(10)
    cookies = driver.get_cookies()
    pickle.dump(cookies, open('facebook.pkl', 'wb'))

    time.sleep(5)


def load_cookies():
    driver = webdriver.Chrome()
    cookie_list = pickle.load(open('facebook.pkl', "rb"))
    url = 'https://web.facebook.com'
    driver.get(url)
    for cookie in cookie_list:
        cookie['domain'] = '.facebook.com'
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(e)
    driver.get(url)
    time.sleep(20)


login()
load_cookies()
