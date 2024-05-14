import time
import pytest
from .pages.location_popup import Lock
from .pages.main_page import MainPage
from .pages.auth import Auth
from selenium import webdriver
# driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .pages.basket_page import Basket


# def test_check_save_user_location(browser):
#     link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
#     page = Lock(browser, link)
#     page.open()
#     browser.implicitly_wait(5)
#     page.change_location()
#     time.sleep(10)
#     browser.implicitly_wait(5)
#     page = Auth(browser, link)
#     page.auth_tg()
#     browser.implicitly_wait(10)
#     page.input_code()
#     time.sleep(3)
#     page.skip_popup_bonus()
#     time.sleep(10)
#     page = MainPage(browser, link)
#     page.open_burger_menu()
#     time.sleep(5)
#     page.check_location()


# def test_add_item_to_basket_from_popup_unauth_user(browser):
#     link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
#     page = Lock(browser, link)
#     page.open()
#     browser.implicitly_wait(5)
#     page.start_location_close()
#     browser.implicitly_wait(5)
#     page = MainPage(browser, link)
#     page.add_item_to_basket_from_popup_unauth_user()
#     time.sleep(3)
#
#
# def test_add_item_to_basket_from_main_unauth_user_without_mod(browser):
#     link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
#     page = Lock(browser, link)
#     page.open()
#     time.sleep(3)
#     page.start_location_close()
#     time.sleep(3)
#     page = MainPage(browser, link)
#     time.sleep(3)
#     page.add_item_to_basket_from_main_unauth_user_without_mod()
#     time.sleep(3)
#
#
# def test_add_item_to_basket_from_popup_unauth_user_without_mod(browser):
#     link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
#     page = Lock(browser, link)
#     page.open()
#     time.sleep(3)
#     page.start_location_close()
#     time.sleep(3)
#     page = MainPage(browser, link)
#     time.sleep(3)
#     page.add_item_to_basket_from_popup_unauth_user_without_mod()
#     time.sleep(3)
#
# def test_add_to_favorites_in_main_unauth_user(browser):
#     link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
#     page = Lock(browser, link)
#     page.open()
#     time.sleep(3)
#     page.start_location_close()
#     time.sleep(3)
#     page = MainPage(browser, link)
#     time.sleep(3)
#     page.add_to_favorites_in_main_unauth_user()
#     time.sleep(3)
#
#
# def test_add_to_favorites_in_popup_unauth_user(browser):
#     link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
#     page = Lock(browser, link)
#     page.open()
#     time.sleep(3)
#     page.start_location_close()
#     time.sleep(3)
#     page = MainPage(browser, link)
#     time.sleep(3)
#     page.add_to_favorites_in_popup_unauth_user()
#     time.sleep(3)

def test_push_success_add_to_basket(browser):
    link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
    page = Lock(browser, link)
    page.open()
    time.sleep(3)
    page.start_location_close()
    time.sleep(3)
    page = Auth(browser, link)
    browser.implicitly_wait(20)
    page.auth_tg()
    time.sleep(3)
    page.input_code()
    browser.implicitly_wait(20)
    page.skip_popup_bonus()
    time.sleep(3)
    page = Basket(browser, link)
    page.add_item_to_basket()
    browser.implicitly_wait(10)
    page.check_push()






