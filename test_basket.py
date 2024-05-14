import time
import pytest
from .pages.location_popup import Lock
from .pages.basket_page import Basket
from .pages.auth import Auth
from selenium import webdriver
# driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_delete_all_goods(browser):
    link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
    page = Lock(browser, link)
    page.open()
    time.sleep(3)
    page.start_location_close()
    time.sleep(3)
    page = Auth(browser, link)
    page.auth_tg()
    page.input_code()
    time.sleep(3)
    page.skip_popup_bonus()
    time.sleep(3)
    page = Basket(browser, link)
    page.delete_all_goods()
    time.sleep(3)


def test_add_favorite(browser):
    link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
    page = Lock(browser, link)
    page.open()
    time.sleep(3)
    page.start_location_close()
    time.sleep(3)
    page = Auth(browser, link)
    page.auth_tg()
    page.input_code()
    time.sleep(3)
    page.skip_popup_bonus()
    time.sleep(1)
    page = Basket(browser, link)
    page.add_favorite()
    time.sleep(3)


def test_change_quantity_goods(browser):
    link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
    page = Lock(browser, link)
    page.open()
    time.sleep(3)
    page.start_location_close()
    time.sleep(3)
    page = Auth(browser, link)
    page.auth_tg()
    page.input_code()
    time.sleep(3)
    page.skip_popup_bonus()
    time.sleep(1)
    page = Basket(browser, link)
    page.change_quantity_goods()
    time.sleep(3)