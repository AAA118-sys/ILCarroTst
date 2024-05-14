import time
from .base_page import BasePage
from .locators import ModPopupLocators
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ModPopup(BasePage):
    def check_change_price(self):
        self.open_item()
        time.sleep(5)
        self.change_v()
        time.sleep(5)
        self.price()
        time.sleep(5)

    def check_standart_mod(self):
        self.open_item()
        time.sleep(5)
        self.button_standart()
        time.sleep(5)
        self.should_not_be_block_mod()
        time.sleep(5)

    def add_to_basket_item_with_mod(self):
        self.open_item()
        time.sleep(5)
        self.taste_mod()
        time.sleep(5)
        self.honey_mod()
        time.sleep(5)
        self.third_mod()
        time.sleep(5)
        self.suger_mod()
        time.sleep(5)
        self.suger_mod()
        time.sleep(5)
        self.add_o_basket()
        time.sleep(5)

    def open_item(self):
        Open_item = self.browser.find_element(*ModPopupLocators.CARD)
        Open_item.click()

    def change_v(self):
        Change_v = self.browser.find_element(*ModPopupLocators.ANOTHER_V)
        Change_v.click()

    def price(self):
        price = self.browser.find_element(*ModPopupLocators.PRICE)
        price = price.text
        assert price == "200 ₽", \
            "znac ne sovpadaet"
        assert True

    def button_standart(self):
        Button_standart = self.browser.find_element(*ModPopupLocators.BUTTON_STANDART)
        Button_standart.click()

    def should_not_be_block_mod(self):
        assert self.is_not_element_present(*ModPopupLocators.MOD_BLOCK), \
            "Mod block is  presented, but shouldn't be"

    def taste_mod(self):
        Taste_mod = self.browser.find_element(*ModPopupLocators.TASTE_MOD)
        Taste_mod.click()

    def honey_mod(self):
        Honey_mod = self.browser.find_element(*ModPopupLocators.HONEY_MOD)
        self.browser.execute_script("arguments[0].click();", Honey_mod)

    def third_mod(self):
        Third_mod = self.browser.find_element(*ModPopupLocators.THIRD_MOD)
        self.browser.execute_script("arguments[0].click();", Third_mod)

    def suger_mod(self):
        Suger_mod = self.browser.find_element(*ModPopupLocators.SUGAR_MOD)
        self.browser.execute_script("arguments[0].click();", Suger_mod)

    def add_o_basket(self):
        Add_o_basket = self.browser.find_element(*ModPopupLocators.ADD_TO_BASKET)
        Add_o_basket.click()