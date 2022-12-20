from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://web.facebook.com/?_rdc=1&_rdr'

driver.get(url)

user_name = driver.find_element(By.XPATH, value="//input[@id='email']")
password = driver.find_element(By.XPATH, value="//input[@id='pass']")
submit = driver.find_element(By.XPATH, value='//*[@id="u_0_9_p0"]')

user_name.send_keys("s.hygienic@yahoo.com")
password.send_keys('!s0249612579!SS')
submit.click()
time.sleep(30)