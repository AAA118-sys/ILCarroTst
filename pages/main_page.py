import time
from .base_page import BasePage
from .locators import MainLocators
from selenium import webdriver
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


    def add_item_to_basket_from_popup_unauth_user(self):
        self.open_popup()
        driver.implicitly_wait(5)
        self.add_to_basket_in_popup()
        driver.implicitly_wait(5)
        self.should_be_auth_popup()

    def add_item_to_basket_from_main_unauth_user_without_mod(self):
        self.add_to_basket_in_main_without_mod()
        driver.implicitly_wait(10)
        self.should_be_auth_popup()
        driver.implicitly_wait(10)

    def add_item_to_basket_from_popup_unauth_user_without_mod(self):
        self.open_popup_item_without_mod()
        driver.implicitly_wait(10)
        self.add_to_basket_in_popup_without_mod()
        driver.implicitly_wait(10)
        self.should_be_auth_popup()
        driver.implicitly_wait(10)

    def add_to_favorites_in_main_unauth_user(self):
        self.add_to_favorites_in_main()
        driver.implicitly_wait(10)
        self.should_be_auth_popup()
        driver.implicitly_wait(10)

    def add_to_favorites_in_popup_unauth_user(self):
        self.add_to_favorites_in_popup()
        driver.implicitly_wait(10)
        self.should_be_auth_popup()
        driver.implicitly_wait(10)

    def open_popup(self):
        Open_popup = self.browser.find_element(*MainLocators.CARD_WITH_MOD)
        Open_popup.click()

    def add_to_basket_in_popup(self):
        Add_to_basket_in_popup = self.browser.find_element(*MainLocators.BUTTON_POPUP_ADD)
        Add_to_basket_in_popup.click()

    def should_be_auth_popup(self):
        assert self.is_element_present(*MainLocators.POPUP_AUTH), \
            "Auth popup is not presented, but should be"

    def add_to_basket_in_main_without_mod(self):
        Add_to_basket_in_main_without_mod = self.browser.find_element(*MainLocators.BUTTON_ADD_ITEM_WITHOUT_MOD)
        Add_to_basket_in_main_without_mod.click()

    def open_popup_item_without_mod(self):
        Add_to_basket_in_main_without_mod = self.browser.find_element(*MainLocators.BUTTON_OPEN_POPUP_WITHOUT_MOD)
        Add_to_basket_in_main_without_mod.click()

    def add_to_basket_in_popup_without_mod(self):
        Add_to_basket_in_main_without_mod = self.browser.find_element(*MainLocators.BUTTON_ADD_ITEM_WITHOUT_MOD_IN_POPUP)
        Add_to_basket_in_main_without_mod.click()

    def add_to_favorites_in_main(self):
        add_to_favorites_in_main = self.browser.find_element(*MainLocators.BUTTON_FAVORITES_IN_MAIN)
        add_to_favorites_in_main.click()

    def add_to_favorites_in_popup(self):
        add_to_favorites_in_main = self.browser.find_element(*MainLocators.BUTTON_FAVORITES_IN_POPUP)
        add_to_favorites_in_main.click()

    def open_burger_menu(self):
        Open_burger_menu = self.browser.find_element(*MainLocators.OPEN_BURGER_MENU)
        Open_burger_menu.click()

    def check_location(self):
        Check_location = self.browser.find_element(*MainLocators.CHECK_LOCATION)
        Check_location = Check_location.text
        assert Check_location == "Ливанова 5", \
            "znac ne sovpadaet"
        assert True
