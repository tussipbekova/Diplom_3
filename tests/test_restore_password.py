import time

import allure
import pytest

from data.data import email
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage


class TestRestorePassword:

    @allure.title('Проверка восстановления пароля')
    @allure.description(
        'На странице восстановления пароля при клике по кнопке показать/скрыть пароль  поле  подсвечивается.')
    def test_restore_password(self, driver):
        main_page = MainPage(driver)

        # ожидаем появления на странице заголовка Соберите бургер
        main_page.wait_for_load_home_page()

        # кликаем по кнопке Войти в аккаунт
        main_page.click_to_login_button()

        login_page = LoginPage(driver)

        # ожидаем появления на странице заголовка Вход
        login_page.wait_for_load_main_field()

        # кликаем по cсылке Восстановить пароль
        login_page.click_to_restore_password_link()

        forgot_password_page = ForgotPasswordPage(driver)

        # ожидаем появления на странице кнопки Восстановить
        forgot_password_page.wait_for_load_restore_button()

        # заполняем поле email
        forgot_password_page.set_email(email)

        # кликаем по cсылке Восстановить
        forgot_password_page.click_to_restore_button()

        reset_password_page = ResetPasswordPage(driver)

        # ожидаем появления на странице кнопки Сохранить
        reset_password_page.wait_for_load_show_hide_password_button()
        time.sleep(2)
        # кликаем по кнопке показать/скрыть пароль
        reset_password_page.click_to_show_hide_password()

        # достаем активное поле с подсветкой
        active_field = reset_password_page.get_active_password_field()

        assert active_field != None
