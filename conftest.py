import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options


def pytest_addoption(parser):		#Запрашиваем у юзера браузер и язык
    parser.addoption('--browser', action ='store', default = "chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action = "store", default = "en",
    				help = "Choose language")

@pytest.fixture(scope="function")
def browser(request):				#вызываем и отдаём выбранный браузер  с выбранной локалью
    browser_name = request.config.getoption("browser")
    user_language = request.config.getoption("language")

    if browser_name == "chrome": #Хром
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options = options)

    elif browser_name == "firefox":	#файрфокс
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile = fp)

    else:	#опечатка/неизвестный браузер - запускается хром, локаль - en-gb
        print (f"\nBrowser {browser_name} is still not implemented, starting Chrome by default")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options = options)
        
    yield browser
    print("\nquit browser..")
    browser.quit()