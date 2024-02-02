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

    @allure.step('Клик по кнопке Личный кабинет')
    def click_to_personal_account_button(self):
        self.click(personal_account_button)

    @allure.step('Клик по кнопке Конструктор')
    def click_to_constructor_button(self):
        self.click(constructor_button_locator)

    @allure.step('Клик по кнопке Лента заказов')
    def click_to_ordered_feed(self):
        self.click(ordered_feed_locator)

    @allure.step('Клик по инредиенту')
    def click_to_ingredient(self):
        self.click(ingredient_locator)

    @allure.step('Достаем всплывающее окно')
    def get_pop_up_window_module(self):
        return self.get_element(pop_up_window_locator)



