from selenium.webdriver.common.by import By


class LocationPopup():
    BUTTON_CHOOSE_ADDRESS = (By.XPATH, "//div[@class='select__label']")
    SELECTOR_LOCATIONS = (By.CSS_SELECTOR, ".select__list > .select__list-item:nth-child(5)")
    BUTTON_SAVE = (By.XPATH, "//button[@class='button button--primary pick-up-point-modal__button']")
    OPEN_POPUP = (By.XPATH, "//*[@id='app']/div[1]/div/div/div/div[1]/div")
    SELECTOR_LOCATIONS_ANOTHER = (By.CSS_SELECTOR, ".select__list > .select__list-item:nth-child(4)")


class AuthLocators():
    BUTTON_AUTH = (By.XPATH, "//button[@class='button button--primary log-in']")
    INPUT_PHONE = (By.XPATH, "//*[@id='auth-phone']")
    BUTTON_TG = (By.XPATH, "//button[@class='button button--primary auth-form__button auth-form__button_telegram']")
    BUTTON_SMS = (By.XPATH, "//button[@class='button button--outline auth-form__button auth-form__button_phone']")
    BUTTON_CODE_1 = (By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div[1]/input")
    BUTTON_CODE_2 = (By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div[2]/input")
    BUTTON_CODE_3 = (By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div[3]/input")
    BUTTON_CODE_4 = (By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div[4]/input")
    EL_PROBLEMS = (By.XPATH, "//div[@class='auth-form__problems']")
    CLOSE_POPUP_BONUS = (By.XPATH, "/html/body/div[4]/div/button")
    TITLE_LK = (By.XPATH, "//*[@id='app']/div[2]/div/div/h1")


class MainLocators():
    CARD_WITH_MOD = (By.CSS_SELECTOR, ".category-block__products > .card.card-desktop:nth-child(1)")
    BUTTON_POPUP_ADD = (By.XPATH, "//button[@class='button button--primary detailed-modal__btn-full']")
    BUTTON_ADD_ITEM_WITHOUT_MOD = (By.XPATH, "//*[@id='id2']/div/div[3]/div[2]/div[2]/div[2]/div")
    POPUP_AUTH = (By.XPATH, "/html/body/div[4]/div/div/form")
    BUTTON_OPEN_POPUP_WITHOUT_MOD = (By.XPATH, "//*[@id='id2']/div/div[3]/div[2]/div[1]/h3")
    BUTTON_ADD_ITEM_WITHOUT_MOD_IN_POPUP = (By.XPATH, "/html/body/div[4]/div/div/div[3]/div/button")
    BUTTON_FAVORITES_IN_MAIN = (By.XPATH, "//*[@id='id1']/div/div[1]/div[1]/button/span/div/svg/g/g/g[1]/g[2]/path")
    BUTTON_FAVORITES_IN_POPUP = (
    By.XPATH, "/html/body/div[4]/div/div/div[1]/div[3]/div[1]/button/span/div/svg/g/g/g[1]/g[2]/path")
    CHECK_LOCATION = (By.XPATH, "//*[@id='app']/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div/span[1]")
    OPEN_BURGER_MENU = (By.XPATH, "//*[@id='app']/div[1]/div/div/div[1]/div[2]/div/button")


class ModPopupLocators():
    CARD = (By.XPATH, "//*[@id='id1']/div/div[3]/div[2]/div[1]")
    ANOTHER_V = (By.XPATH, "/html/body/div[4]/div/div/div[1]/div[3]/div[6]/div/span[2]")
    PRICE = (By.XPATH, "/html/body/div[4]/div/div/div[3]/div/div")
    MOD_BLOCK = (By.XPATH, "/html/body/div[4]/div/div/div[2]/div[1]/div[1]")
    BUTTON_STANDART = (By.XPATH, "/html/body/div[4]/div/div/div[1]/div[3]/div[7]/button[2]")
    TASTE_MOD = (By.XPATH, "/html/body/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/button")
    HONEY_MOD = (By.XPATH, "/html/body/div[4]/div/div/div[2]/div[2]/div[2]/div[3]/button")
    THIRD_MOD = (By.XPATH, "/html/body/div[4]/div/div/div[2]/div[3]/div[2]/div[2]/button")
    SUGAR_MOD = (By.XPATH, "/html/body/div[4]/div/div/div[2]/div[4]/div[2]/div[2]/div/div/button[2]")
    ADD_TO_BASKET = (By.XPATH, "/html/body/div[4]/div/div/div[3]/div/button")


class BasketLocators():
    CARD = (By.XPATH, "//*[@id='id2']/div/div[1]/div[2]/div[2]/div[2]/div/div/button[2]")
    BUTTON_BASKET_IN = (By.CSS_SELECTOR,
                        "#app > div.layout.layout_dark.layout_full-height > div > div > div.header > div.actions.header__actions > button.button.button--primary.with-counter.basket")
    BUTTON_REMOTE_ALL_GOODS = (By.XPATH, "//*[@id='app']/div[2]/div/div/div[2]/div[1]/div/div/div[1]/button/span")
    BUTTON_ADD_FAVORITE = (
    By.XPATH, "//*[@id='app']/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div[6]/div[1]/button")
    CLEAR_BASKET = (By.XPATH, "//*[@id='app']/div[2]/div/div/div[3]/div/div[2]")
    BUTTON_FAVORITE_PAGE = (By.XPATH, "//*[@id='app']/div[1]/div/div/div/div[5]/button[1]")
    ITEM_IN_FAVORITES = (By.XPATH, "//*[@id='app']/div[2]/div/div/div/div/div/div/div[1]/div[2]/div[1]")
    BUTTON_SWITCH = (
    By.XPATH, "//*[@id='app']/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/div[4]/div/div/button[2]")
    TOTAL_PRICE = (By.XPATH, "//*[@id='app']/div[2]/div/div/div[2]/div[2]/div/div/div[4]/span")
    BUTTON_ORDER_TO = (By.XPATH, "//*[@id='app']/div[2]/div/div/div[2]/div[2]/button")
    PUSH_SUCCESS_ADD_TO_BASKET = (By.XPATH, "//*[@id='app']/div[5]/div/div/div/div")


class OrderLocators():
    COMMENT_IN = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/div/form/div[1]/div[1]/div[3]/textarea")
    BUTTON_PAY = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/div/form/div[2]/button")
    UMONEY_CHECK_ELEMENT = (By.XPATH, "//*[@id='root']/div/div[1]/div[3]/div[1]/a")
