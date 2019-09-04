from selenium.webdriver.common.by import By

class MainPageLocators(object):
    pass

class LoginPageLocators(object):
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_RETRIEVE_PASSWORD_LINK = (By.CSS_SELECTOR, "#content_inner p a")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")

    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators(object):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR,".product_main h1")
    PRODUCT_PRICE_DESCRIPTION = (By.CSS_SELECTOR,".product_main .price_color")
    TOTAL_PRICE_BASKET = (By.CSS_SELECTOR,".basket-mini")
    PRODUCT_PRICE_ALERT = (By.CSS_SELECTOR,"#messages>:nth-child(3) strong")
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR,"#messages>:nth-child(1) strong")

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


    


