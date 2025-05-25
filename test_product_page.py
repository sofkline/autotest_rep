import time

import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import PageObject


@pytest.mark.need_review
@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_guest_can_add_product_to_basket(browser, link):
    page = PageObject(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.send_message()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = PageObject(browser, "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = PageObject(browser, "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = PageObject(browser, "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    page.open()
    page.add_to_cart()
    page.should_disappear()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    page = PageObject(browser, "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    page.open()

    # Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    basket_page = BasketPage(browser, page.browser.current_url)

    # Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_emty_basket_text()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = PageObject(browser, "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    page.open()
    page.go_to_login_page()
    LoginPage(browser, page.browser.current_url).should_be_login_page()


@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = PageObject(browser, "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
        page.open()
        page.go_to_login_page()
        registration_page = LoginPage(browser, page.browser.current_url)
        registration_page.register_new_user(f"{time.time()}@fakemail.com", "SuperSEcure34234passdfew")
        registration_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = PageObject(
            browser,
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        )
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.send_message()
