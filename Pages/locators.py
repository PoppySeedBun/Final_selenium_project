from selenium.webdriver.common.by import By

class MainPageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")
	
class LoginPageLocators(object):
	LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
	LOGIN_PASSWPRD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
	LOGIN_RETRIEVE_PASSWORD_LINK = (By.CSS_SELECTOR, "#content_inner p a")
	LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")

	REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTRATION_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")