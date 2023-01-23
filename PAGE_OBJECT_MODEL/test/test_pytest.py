import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures('setup')
class TestClick:
    def test_click(self):
        """clicking to close a cooking popup"""
        self.driver.find_element(By.XPATH, '//*[@id="ccc-notify-accept"]').click()
        time.sleep(3)

        # switching to page frame
        iframe = self.driver.find_element(By.XPATH, '//iframe[@title="Money Navigator tool"]')
        self.driver.switch_to.frame(iframe)
        time.sleep(3)

        """the button which is an anchor tag i have been trying to click"""
        self.driver.find_element(By.XPATH, "//div[@class='landing__actions']//a").click()
        time.sleep(3)

    def test_func(self):
        print('run once')

    def test_try(self):
        print('printfdlfadf')
        time.sleep(5)
