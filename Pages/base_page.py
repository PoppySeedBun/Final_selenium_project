from .locators import BasePageLocators
from .locators import MainPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


class BasePage(object):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how,what)
        except NoSuchElementException:
            return False
        return True
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12*math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f"Your code:{alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how,what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how,what)))
        except TimeoutException:
            return True
        return False

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        assert self.browser.current_url == self.browser.find_element(*BasePageLocators.LOGIN_LINK).get_attribute("href"), \
        "Link doesn't redirect to the login page"

    def go_to_basket(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        url_to_be_redirected = self.browser.find_element(*MainPageLocators.BASKET_BUTTON).get_attribute("href")
        link.click()
        assert  self.browser.current_url == url_to_be_redirected, "Link doesn't redirect to the basket page"
       
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented,"\
                                                                     " probably unauthorised user"


               




