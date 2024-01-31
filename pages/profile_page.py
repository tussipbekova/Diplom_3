import allure

from locators.profile_locators import exit_button_locator, orders_history_locator, order_history_list_locator
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Ожидание загрузки кнопки Выход')
    def wait_for_load_exit_button(self):
        self.wait_for_visibility(exit_button_locator)

    @allure.step('Клик по кнопке  История заказов для перехода в этот раздел')
    def click_to_orders_history_link(self):
        self.click(orders_history_locator)

    @allure.step('Достаем список заказов')
    def get_orders_list(self):
        return self.get_element(order_history_list_locator)

    @allure.step('Клик по кнопке  Выход')
    def click_to_exit_link(self):
        self.click(exit_button_locator)

