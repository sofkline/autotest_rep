from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "It's not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No login form found!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "No register form found!"

    def register_new_user(self, email: str, password: str):
        self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_INPUT_EMAIL
        ).send_keys(email)

        self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_INPUT_PASSWORD
        ).send_keys(password)

        self.browser.find_element(
            *LoginPageLocators.REGISTER_FORM_INPUT_PASSWORD_CONFIRMATION
        ).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT_BTN).click()