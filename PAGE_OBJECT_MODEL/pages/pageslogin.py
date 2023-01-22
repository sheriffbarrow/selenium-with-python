import time
from selenium.webdriver.common.by import By
from PAGE_OBJECT_MODEL.locators.locators import LoginLocator, ProfilePage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, LoginLocator.locator_email).send_keys(email)
        time.sleep(3)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, LoginLocator.locator_password).send_keys(password)
        time.sleep(3)

    def click_login(self):
        self.driver.find_element(By.NAME, LoginLocator.locator_button).click()
        time.sleep(3)

