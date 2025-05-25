from .base_page import BasePage
from .locators import ProductPageLocators


class PageObject(BasePage):

    def add_to_cart(self):
        self.has_product_button()
        self.click_add_to_cart()

    def send_message(self):
        self.send_message_of_product_added_to_cart()
        self.send_message_cost_added_to_cart()

    def has_product_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "No add to cart button found!"

    def click_add_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart.click()

    def send_message_of_product_added_to_cart(self):
        name_of_product_expected = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_EXPECTED).text
        name_of_product_actual = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_ACTUAL).text
        assert name_of_product_expected == name_of_product_actual, f"Name of product should be {name_of_product_expected}, but got {name_of_product_actual}"
        print(f"{name_of_product_actual} added to cart")

    def send_message_cost_added_to_cart(self):
        cost_of_product_expected = self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCT_EXPECTED).text
        cost_of_product_actual = self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCT_ACTUAL).text
        assert cost_of_product_expected == cost_of_product_actual, f"Cost of product should be {cost_of_product_expected}, but got {cost_of_product_actual}"
        print(f"{cost_of_product_actual} added to cart")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Message did not disappear, though it should have"
