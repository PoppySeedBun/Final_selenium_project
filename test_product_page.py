import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.locators import LoginPageLocators
import time


product_base_link = ProductPageLocators.SAMPLE_PRODUCT_PAGE_URL
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(1)] #Left only one link for time saving purposes


@pytest.mark.basket_test
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = LoginPageLocators.LOGIN_PAGE_URL
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.xyz"
        password = "fakepassw0rd"
        page.register_new_user(email, password)
        page.should_be_authorized()
    
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', urls)
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.prices_should_match()
        page.names_should_match()

    def test_user_cant_see_success_message_after_adding_product_to_cart(self, browser):
        link = ProductPageLocators.BROKEN_PRODUCT_PAGE_URL
        page = ProductPage(browser, link)
        page.open()
        page.should_be_no_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.prices_should_match()
    page.names_should_match()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.SAMPLE_PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_no_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.SAMPLE_PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.alert_should_dissapear()  

def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.SAMPLE_PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_be_no_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = ProductPageLocators.SAMPLE_PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLocators.SAMPLE_PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.SAMPLE_PRODUCT_PAGE_URL
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.test_there_is_empty_basket_message()
    basket_page.test_there_is_no_items_in_basket()
