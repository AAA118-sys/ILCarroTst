import time
import pytest
from .pages.location_popup import Lock
from .pages.basket_page import Basket
from .pages.mod_popup import ModPopup
from .pages.order_page import Order
from .pages.auth import Auth
from selenium import webdriver
# driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_order_goods_with_quantity_2(browser):
    link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
    page = Lock(browser, link)
    page.open()
    time.sleep(3)
    page.start_location_close()
    time.sleep(3)
    page = Auth(browser, link)
    time.sleep(5)
    page.auth_tg()
    time.sleep(5)
    page.input_code()
    time.sleep(5)
    page.skip_popup_bonus()
    time.sleep(5)
    page = Basket(browser, link)
    page.order_in_item_with_2_quantity()
    time.sleep(10)
    page = Order(browser, link)
    page.go_to_pay()
    time.sleep(5)


# def test_order_item_with_mod(browser):
#     link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
#     page = Lock(browser, link)
#     page.open()
#     page.start_location_close()
#     time.sleep(5)
#     page = Auth(browser, link)
#     page.auth_tg()
#     time.sleep(5)
#     page.input_code()
#     time.sleep(5)
#     page.skip_popup_bonus()
#     time.sleep(5)
#     page = ModPopup(browser, link)
#     page.add_to_basket_item_with_mod()
#     page = Basket(browser, link)
#     page.open_basket()
#     page.order_button()
#     page = Order(browser, link)
#     page.go_to_pay()