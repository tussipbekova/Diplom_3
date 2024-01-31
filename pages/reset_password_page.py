import allure

from locators.main_locators import *
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):


    @allure.step('Ожидание загрузки кнопке показать/скрыть пароль')
    def wait_for_load_show_hide_password_button(self):
        self.wait_for_clickable(show_hide_password_button_locator)

    @allure.step('Клик по кнопке показать/скрыть пароль ')
    def click_to_show_hide_password(self):
        self.click(show_hide_password_button_locator)

    @allure.step('Достаем поле с подсветкой ')
    def get_active_password_field(self):
        return self.get_element(active_password_field_locator)
