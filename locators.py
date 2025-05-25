from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_INPUT_EMAIL = (By.ID, "id_registration-email")
    REGISTER_FORM_INPUT_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_FORM_INPUT_PASSWORD_CONFIRMATION = (By.ID, "id_registration-password2")
    REGISTER_FORM_SUBMIT_BTN = (By.CSS_SELECTOR, "button[name=registration_submit]")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_OF_PRODUCT_ACTUAL = (By.CSS_SELECTOR, "div.alertinner strong")
    NAME_OF_PRODUCT_EXPECTED = (By.CSS_SELECTOR, "div.product_main h1")
    COST_OF_PRODUCT_ACTUAL = (By.CSS_SELECTOR, "#messages div.alert.alert-safe.alert-noicon.alert-info.fade.in div p:nth-child(1) strong")
    COST_OF_PRODUCT_EXPECTED = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner ")

class BasketPageLocators:
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
