import allure

from locators.forgot_password_locators import restore_button_locator, email_field_locator
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):


    @allure.step('Ожидание загрузки кнопки Восстановить')
    def wait_for_load_restore_button(self):
        self.wait_for_visibility(restore_button_locator)

    @allure.step('Заполнение поля email')
    def set_email(self, email):
        self.send_keys(email_field_locator, email)

    @allure.step('Клик по кнопке Восстановить')
    def click_to_restore_button(self):
        self.click(restore_button_locator)
