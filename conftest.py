import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="function")
def driver():
    #firefox_driver = GeckoDriverManager().install()
    #service = FS(firefox_driver)
    driver = webdriver.Firefox()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver

    driver.quit()