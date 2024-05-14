import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()


class Basket(BasePage):
    def delete_all_goods(self):
        self.add_item_to_basket()
        driver.implicitly_wait(10)
        self.open_basket()
        driver.implicitly_wait(10)
        self.remote_all_goods()
        driver.implicitly_wait(10)
        self.should_be_block_clear_basket()
        driver.implicitly_wait(10)

    def add_favorite(self):
        self.add_item_to_basket()
        driver.implicitly_wait(10)
        self.open_basket()
        driver.implicitly_wait(10)
        self.add_favorite_item()
        driver.implicitly_wait(10)
        self.open_favorite()
        driver.implicitly_wait(10)
        self.should_be_item_in_favorites()
        driver.implicitly_wait(10)

    def change_quantity_goods(self):
        self.add_item_to_basket()
        driver.implicitly_wait(10)
        self.open_basket()
        driver.implicitly_wait(10)
        self.switch_kol()
        driver.implicitly_wait(10)
        self.total_price()
        driver.implicitly_wait(10)

    def order_in_item_with_2_quantity(self):
        self.add_item_to_basket()
        time.sleep(5)
        self.open_basket()
        time.sleep(5)
        self.switch_kol()
        time.sleep(5)
        self.order_button()
        time.sleep(5)

    def add_item_to_basket(self):
        Add_item_to_basket = self.browser.find_element(*BasketLocators.CARD)
        Add_item_to_basket.click()

    def open_basket(self):
        Open_basket = self.browser.find_element(*BasketLocators.BUTTON_BASKET_IN)
        self.browser.execute_script("arguments[0].click();", Open_basket)

    def remote_all_goods(self):
        Remote_all_goods = self.browser.find_element(*BasketLocators.BUTTON_REMOTE_ALL_GOODS)
        Remote_all_goods.click()

    def add_favorite_item(self):
        Add_favorite = self.browser.find_element(*BasketLocators.BUTTON_ADD_FAVORITE)
        Add_favorite.click()

    def open_favorite(self):
        Open_favorite = self.browser.find_element(*BasketLocators.BUTTON_FAVORITE_PAGE)
        Open_favorite.click()

    def should_be_block_clear_basket(self):
        assert self.is_element_present(*BasketLocators.CLEAR_BASKET), \
            "goods have not been deleted"

    def should_be_item_in_favorites(self):
        assert self.is_element_present(*BasketLocators.ITEM_IN_FAVORITES), \
            "goods have not been deleted"

    def switch_kol(self):
        Switch_kol = self.browser.find_element(*BasketLocators.BUTTON_SWITCH)
        Switch_kol.click()

    def total_price(self):
        Total_price = self.browser.find_element(*BasketLocators.TOTAL_PRICE)
        Total_price = Total_price.text
        assert Total_price == "580 ₽", \
            "switch doesnt work"
        assert True

    def order_button(self):
        Order_button = self.browser.find_element(*BasketLocators.BUTTON_ORDER_TO)
        Order_button.click()
        # self.browser.execute_script("arguments[0].click();", Order_button)

    def check_push(self):
        assert self.is_element_present(*BasketLocators.PUSH_SUCCESS_ADD_TO_BASKET), \
            "push isn't present"



