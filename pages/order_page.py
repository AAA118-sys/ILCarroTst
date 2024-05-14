import time
from .base_page import BasePage
from .locators import OrderLocators
from selenium import webdriver
browser = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Order(BasePage):
    def go_to_pay(self):
        self.comment_in()
        browser.implicitly_wait(20)
        self.pay_to()
        browser.implicitly_wait(20)
        self.u_check_in()

    def comment_in(self):
        Comment_in = self.browser.find_element(*OrderLocators.COMMENT_IN)
        Comment_in.send_keys("Тест не выполнять!")

    def pay_to(self):
        Pay_to = self.browser.find_element(*OrderLocators.BUTTON_PAY)
        Pay_to.click()

    def u_check_in(self):
        assert self.is_element_present(*OrderLocators.UMONEY_CHECK_ELEMENT), \
            "user isnt on page umoney"
