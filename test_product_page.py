import pytest
from .pages.product_page import ProductPage


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_to_basket(browser,link):
	page = ProductPage(browser,link)
	page.open()
	page.add_to_basket()
	page.prices_should_match()
	page.names_should_match()

@pytest.mark.find
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer7"
	page = ProductPage(browser,link)
	page.open()
	page.should_be_no_success_message_two()



	

	
