import time

import allure
import pytest

from conftest import driver
from data.data import email, password
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestPersonalAccount:

    @allure.title('Личный кабинет')
    @allure.description('Проверить, в личном кабинете кнопку  история заказов и кнопку выход из аккаунта')
    def test_personal_account(self, driver):
        main_page = MainPage(driver)

        # ожидаем появления на странице заголовка Соберите бургер
        main_page.wait_for_load_home_page()

        # кликаем по кнопке Личный кабинет
        main_page.click_to_personal_account_button()

        login_page = LoginPage(driver)

        # ожидаем появления на странице заголовка Вход
        login_page.wait_for_load_main_field()

        # заполняем поле email
        login_page.set_email(email)

        # заполняем поле password
        login_page.set_password(password)

        # кликаем по кнопке Войти
        login_page.click_to_login_button()

        # ожидаем появления на странице заголовка Соберите бургер
        main_page.wait_for_load_home_page()

        # кликаем по кнопке Личный кабинет
        main_page.click_to_personal_account_button()


        profile_page = ProfilePage(driver)
        # ожидаем появления на странице кнопки Выход
        profile_page.wait_for_load_exit_button()
        time.sleep(2)
        # кликаем по кнопке История заказов
        profile_page.click_to_orders_history_link()

        orders_history = profile_page.get_orders_list()

        assert orders_history != None

        profile_page.click_to_exit_link()

        login_page.wait_for_load_main_field()

        expected_url = 'https://stellarburgers.nomoreparties.site/login'

        assert expected_url == driver.current_url

























