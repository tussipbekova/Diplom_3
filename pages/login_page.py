import allure

from locators.login_locators import restore_password_link_locator, header_login_locator, email_field_locator, \
    password_field_locator, login_button_locator
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Ожидание загрузки заголовка Вход')
    def wait_for_load_main_field(self):
        self.wait_for_visibility(header_login_locator)

    @allure.step('Клик по ссылке Восстановить пароль')
    def click_to_restore_password_link(self):
        self.click(restore_password_link_locator)

    @allure.step('Заполнение поля email')
    def set_email(self, email):
        self.send_keys(email_field_locator, email)

    @allure.step('Заполнение поля password')
    def set_password(self, password):
        self.send_keys(password_field_locator, password)

    @allure.step('Клик по кнопке Войти')
    def click_to_login_button(self):
        self.click(login_button_locator)



