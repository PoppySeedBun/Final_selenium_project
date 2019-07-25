from .base_page import BasePage
from .locators import ProductPageLocators
import time



class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()
        
    def prices_should_match(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERT).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_DESCRIPTION).text,\
               "Alert and description prices don't match"

        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_DESCRIPTION).text in \
               self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_BASKET).text,\
               "Basket and description prices don't match"
               
    def names_should_match(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, \
               "Product names in alert and description don't match"

    def should_be_no_success_message_two(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_ALERT), "Alert shouldn't be visible"





        

       
      



