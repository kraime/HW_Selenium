import time
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    url = "https://demo.opencart.com/"

    def __init__(self, browser):
        self.browser = browser
        self.logger = logging.getLogger(type(self).__name__)

    def get_title(browser, url, title):
        browser.get(url)

    @staticmethod
    def _input_text(element, text):
        element.clear()
        element.click()
        element.send_keys(text)

    def _find_elements(self, locator):
        self.logger.info("Found elements: {}".format(locator))
        return self.browser.find_elements(*locator)

    def _find_element(self, locator):
        self.logger.info("Found element: {}".format(locator))
        return self.browser.find_element(*locator)

    def _wait_element_to_be_presence(self, locator, wait_time=7):
        self.logger.info("Wait for element to be present: {}".format(locator))
        wait = WebDriverWait(self.browser, wait_time)
        element = None
        try:
            element = wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'{element} not found')
        return element

    def _wait_element_to_be_clickable(self, locator, wait_time=8):
        self.logger.info("Wait for element to be clickable: {}".format(locator))
        wait = WebDriverWait(self.browser, wait_time)
        element = None
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f'{element} not clickable')
        return element

    def get(self, url):
        pass
