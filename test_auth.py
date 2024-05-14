import time
from .pages.auth import Auth
from .pages.location_popup import Lock
from selenium import webdriver
# driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_auth_tg(browser):
    link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
    page = Lock(browser, link)
    page.open()
    browser.implicitly_wait(5)
    page.start_location_close()
    browser.implicitly_wait(10)
    page = Auth(browser, link)
    page.auth_tg()
    time.sleep(1)
    page.input_code()
    browser.implicitly_wait(5)
    page.skip_popup_bonus()
    time.sleep(2)
    page.open_popup_auth()
    browser.implicitly_wait(5)
    page.should_be_profile()


def test_auth_sms(browser):
    link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
    page = Lock(browser, link)
    page.open()
    browser.implicitly_wait(5)
    page.start_location_close()
    browser.implicitly_wait(5)
    page = Auth(browser, link)
    page.auth_sms()
    time.sleep(1)
    page.input_code()
    browser.implicitly_wait(5)
    page.skip_popup_bonus()
    time.sleep(2)
    page.open_popup_auth()
    browser.implicitly_wait(5)
    page.should_be_profile()


def test_auth_sms_wrong_code(browser):
    link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
    page = Lock(browser, link)
    page.open()
    browser.implicitly_wait(5)
    page.start_location_close()
    browser.implicitly_wait(5)
    page = Auth(browser, link)
    page.auth_sms()
    time.sleep(1)
    page.input_code_wrong()
    time.sleep(1)
    page.input_code_wrong()
    time.sleep(1)
    page.input_code_wrong()
    time.sleep(3)
    page.should_be_problem_message()


def test_auth_tg_wrong_code(browser):
    link = "https://ilcarro:hr6Ujx3S0iO6lgdB2EYY@dev.ilcarro.ru/"
    page = Lock(browser, link)
    page.open()
    browser.implicitly_wait(5)
    page.start_location_close()
    browser.implicitly_wait(5)
    page = Auth(browser, link)
    page.auth_tg()
    time.sleep(1)
    page.input_code_wrong()
    time.sleep(1)
    page.input_code_wrong()
    time.sleep(1)
    page.input_code_wrong()
    time.sleep(3)
    page.should_be_problem_message()
