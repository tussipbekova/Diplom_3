import allure

from locators.login_page_locators import restore_password_link_locator, header_login_locator
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Ожидание загрузки заголовка Вход')
    def wait_for_load_main_field(self):
        self.wait_for_visibility(header_login_locator)

    @allure.step('Клик по ссылке Восстановить пароль')
    def click_to_restore_password_link(self):
        self.click(restore_password_link_locator)

