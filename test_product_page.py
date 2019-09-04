import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.basket_test
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.xyz"
        password = "fakepassw0rd"
        page.register_new_user(email,password)
        page.should_be_authorized()

    @pytest.mark.parametrize('link', urls)
    def test_user_can_add_to_basket(self, browser, link):
        page = ProductPage(browser,link)
        page.open()
        page.add_to_basket()
        page.prices_should_match()
        page.names_should_match()

    def test_user_cant_see_success_message_after_adding_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer7"
        page = ProductPage(browser,link)
        page.open()
        page.should_be_no_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()





    

    
