import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
import time


class TestClick:
    @pytest.fixture
    def setup(self):
        global driver
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.moneyhelper.org.uk/en/money-troubles/coronavirus/use-our-money-navigator-tool')

        yield
        self.driver.quit()
        print('using yield to quit the browser')

    def test_click(self, setup):
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
