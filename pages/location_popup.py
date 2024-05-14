import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LocationPopup
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()


class Lock(BasePage):
    def start_location_close(self):
        self.choose_address()
        driver.implicitly_wait(10)
        self.selector()
        driver.implicitly_wait(10)
        self.save()
        driver.implicitly_wait(10)

    def change_location(self):
        self.choose_address()
        driver.implicitly_wait(10)
        self.another_locator()
        driver.implicitly_wait(10)
        self.save()
        driver.implicitly_wait(10)

    def choose_address(self):
        Button_choose_address = self.browser.find_element(*LocationPopup.BUTTON_CHOOSE_ADDRESS)
        Button_choose_address.click()

    def another_locator(self):
        Another_locator = self.browser.find_element(*LocationPopup.SELECTOR_LOCATIONS_ANOTHER)
        Another_locator.click()

    def selector(self):
        Selector = self.browser.find_element(*LocationPopup.SELECTOR_LOCATIONS)
        Selector.click()

    def save(self):
        Button_save = self.browser.find_element(*LocationPopup.BUTTON_SAVE)
        Button_save.click()

    def open_popup(self):
        Open_popup = self.browser.find_element(*LocationPopup.OPEN_POPUP)
        Open_popup.click()


