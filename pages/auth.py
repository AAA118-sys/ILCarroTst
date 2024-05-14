import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import AuthLocators
from pynput.keyboard import Key, Controller
from selenium import webdriver
browser = webdriver.Chrome()


class Auth(BasePage):
    def auth_tg(self):
        self.open_popup_auth()
        browser.implicitly_wait(20)
        self.input_phone()
        browser.implicitly_wait(20)
        self.button_tg()
        time.sleep(2)
        self.skip_popup()

    def auth_sms(self):
        self.open_popup_auth()
        browser.implicitly_wait(20)
        self.input_phone()
        browser.implicitly_wait(20)
        self.button_sms()
        time.sleep(2)
        self.skip_popup()

    def open_popup_auth(self):
        Button_auth = self.browser.find_element(*AuthLocators.BUTTON_AUTH)
        Button_auth.click()
        # Button_auth = WebDriverWait(browser, 10).until(
        #     EC.element_to_be_clickable(*AuthLocators.BUTTON_AUTH))
        # Button_auth.click()

    def input_phone(self):
        Input_phone = self.browser.find_element(*AuthLocators.INPUT_PHONE)
        Input_phone.send_keys("1111111111")

    def button_tg(self):
        Button_tg = self.browser.find_element(*AuthLocators.BUTTON_TG)
        Button_tg.click()

    def button_sms(self):
        Button_sms = self.browser.find_element(*AuthLocators.BUTTON_SMS)
        Button_sms.click()

    def input_code(self):
        Input_code = self.browser.find_element(*AuthLocators.BUTTON_CODE_1)
        Input_code.send_keys("1")
        Input_code = self.browser.find_element(*AuthLocators.BUTTON_CODE_2)
        Input_code.send_keys("1")
        Input_code = self.browser.find_element(*AuthLocators.BUTTON_CODE_3)
        Input_code.send_keys("1")
        Input_code = self.browser.find_element(*AuthLocators.BUTTON_CODE_4)
        Input_code.send_keys("1")

    def input_code_wrong(self):
        Input_code = self.browser.find_element(*AuthLocators.BUTTON_CODE_1)
        Input_code.send_keys("2")
        Input_code = self.browser.find_element(*AuthLocators.BUTTON_CODE_2)
        Input_code.send_keys("2")
        Input_code = self.browser.find_element(*AuthLocators.BUTTON_CODE_3)
        Input_code.send_keys("2")
        Input_code = self.browser.find_element(*AuthLocators.BUTTON_CODE_4)
        Input_code.send_keys("2")

    def skip_popup(self):
        keyboard = Controller()
        keyboard.press(Key.enter)

    def skip_popup_bonus(self):
        # WebDriverWait(self.browser, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/button"))
        # ).click()
        Skip_popup_bonus = self.browser.find_element(*AuthLocators.CLOSE_POPUP_BONUS)
        Skip_popup_bonus.click()

    def should_be_problem_message(self):
        assert self.is_element_present(*AuthLocators.EL_PROBLEMS), \
            "Problem message is not presented, but should be"

    def should_be_profile(self):
        assert self.is_element_present(*AuthLocators.TITLE_LK), \
            "Profile is not presented, but should be"