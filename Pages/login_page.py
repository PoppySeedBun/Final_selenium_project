from .base_page import BasePage
from .locators import LoginPageLocators   


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELD), "Email field for login is not presented" 
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD), "Password field for login is not presented" 
        assert self.is_element_present(*LoginPageLocators.LOGIN_RETRIEVE_PASSWORD_LINK), "Retrieve password link is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button link is not presented"  

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_FIELD), "Email field for registration is not presented" 
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD), "Password field for registration is not presented" 
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD), "Confirm password field is not presented" 
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button link is not presented" 