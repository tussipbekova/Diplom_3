
import allure
import pytest
from selenium import webdriver
from helpers.register_user_helper import RegisterUserHelper as u
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver

    driver.quit()


@allure.title('Входим под новым пользователем на сайт')
@pytest.fixture
def login_new_user(driver, create_new_user):
    # регистрируем нового пользователя
    user_data = create_new_user
    email = user_data['email']
    password = user_data['password']
    driver = driver
    login_page = LoginPage(driver)
    login_page.wait_for_load_main_field()
    login_page.set_email(email)
    login_page.set_password(password)
    login_page.click_to_login_button()
    return driver

@allure.title('Создание нового пользователя с помощью API')
@pytest.fixture
def create_new_user():

    # генерируем уникальные данные нового пользователя
    user_data = u.generate_random_user_data()
    # отправляем запрос на создание пользователя
    response = u.try_to_create_user(user_data)
    # получаем токены пользователя
    received_body = response.json()
    auth_token = received_body['accessToken']
    yield user_data

    # удаляем пользователя
    u.try_to_delete_user(auth_token)