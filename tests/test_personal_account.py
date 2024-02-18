import time

import allure

from conftest import driver
from data.data import email, password, LOGIN_URL, URL
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestPersonalAccount:

    @allure.title('Проверка переходов в Личный кабинет,историю заказов и выход из аккаунта ')
    @allure.description('Проверить, в личном кабинете переход по клику на «Личный кабинет»')
    def test_personal_account_login(self, driver):
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

        expected_url = URL

        assert expected_url == driver.current_url

    @allure.description('Проверить, в личном кабинете выход из аккаунта')
    def test_personal_account_logout(self,driver):
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

        profile_page = ProfilePage(driver)
        # ожидаем появления на странице кнопки Выход
        profile_page.wait_for_load_exit_button()
        time.sleep(2)

        profile_page.click_to_exit_link()

        login_page.wait_for_load_main_field()

        expected_url = LOGIN_URL

        assert expected_url == driver.current_url

    @allure.description('Проверить, в личном кабинете переход в раздел «История заказов»')
    def test_personal_account_orders_history(self, driver):
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

        profile_page = ProfilePage(driver)

        # кликаем по кнопке История заказов
        profile_page.click_to_orders_history_link()

        orders_history = profile_page.get_orders_list()

        assert orders_history != None



























