import os.path
import sys
import unittest
from selenium import webdriver
from PAGE_OBJECT_MODEL.pages.pageslogin import LoginPage


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://web.facebook.com/')

    def test_login(self):
        driver = self.driver
        self.login = LoginPage(driver)
        self.login.enter_email('email')
        self.login.enter_password('pass')
        self.login.click_login()

    def tearDown(self):
        driver = self.driver
        driver.quit()


if __name__ == '__name__':
    unittest.main()
