import allure

from data.data import email, FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage


class TestRestorePassword:

    @allure.title('Проверка восстановления пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»,')
    def test_restore_password_with_button(self, driver):
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

        expected_url = FORGOT_PASSWORD_URL

        assert expected_url == driver.current_url

    @allure.description(
        'Переход на страницу восстановления пароля по кнопке «Восстановить пароль» и ввод почты и клик по кнопке «Восстановить»,')
    def test_restore_password_with_email(self, driver):
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

        expected_url = RESET_PASSWORD_URL

        assert expected_url == driver.current_url

    @allure.description(
        'При восстановлении пароля клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_restore_password_with_active_field(self, driver):
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

        # кликаем по кнопке показать/скрыть пароль
        reset_password_page.click_to_show_hide_password()

        # достаем активное поле с подсветкой
        active_field = reset_password_page.get_active_password_field()

        assert active_field is not None
