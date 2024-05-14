import time
import pytest
from .pages.location_popup import Lock
from .pages.mod_popup import ModPopup
from .pages.order_page import Order
from selenium import webdriver
# driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_check_change_price_in_popup(browser):
    link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
    page = Lock(browser, link)
    page.open()
    time.sleep(3)
    page.start_location_close()
    page = ModPopup(browser, link)
    time.sleep(3)
    page.check_change_price()
    time.sleep(3)


def test_check_standart_mod_in_popup(browser):
    link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
    page = Lock(browser, link)
    page.open()
    time.sleep(3)
    page.start_location_close()
    page = ModPopup(browser, link)
    time.sleep(3)
    page.check_standart_mod()
    time.sleep(3)