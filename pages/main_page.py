import allure

from locators.main_locators import *
from pages.base_page import BasePage


class MainPage(BasePage):


    @allure.step('Ожидание загрузки главной страницы')
    def wait_for_load_home_page(self):
        self.wait_for_visibility(main_page_title_locator)

    @allure.step('Клик по кнопке Войти в аккаунт')
    def click_to_login_button(self):
        self.click(login_button_locator)




