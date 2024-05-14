import math
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
# from .locators import BasePageLocators
from .locators import LocationPopup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=1):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def choose_location(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def choose_address(self):
        Button_choose_address = self.browser.find_element(*LocationPopup.BUTTON_CHOOSE_ADDRESS)
        Button_choose_address.click()

    def selector(self):
        Selector = self.browser.find_element(*LocationPopup.SELECTOR_LOCATIONS)
        Selector.click()

    def save(self):
        Button_save = self.browser.find_element(*LocationPopup.BUTTON_SAVE)
        Button_save.click()
