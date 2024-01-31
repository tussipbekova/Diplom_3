import allure

from locators.main_locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):


    @allure.step('Ожидание загрузки заголовка Вход')
    def wait_for_load_main_field(self):
        self.wait_for_visibility(header_login_locator)

    @allure.step('Клик по ссылке Восстановить пароль')
    def click_to_restore_password_link(self):
        self.click(restore_password_link_locator)

