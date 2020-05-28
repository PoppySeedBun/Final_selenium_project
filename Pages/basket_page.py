from base_page import BasePage
from locators import BasketPageLocators


class BasketPage(BasePage):
    def test_there_is_empty_basket_message(self):
        assert BasketPageLocators.BASKET_IS_EMPTY_EN_TEXT in self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_LOCATOR).text, \
        "No 'basket is empty' message or message is wrong"

    def test_there_is_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET_MESSAGE),\
                 "Basket should be empty, but it isn't"
