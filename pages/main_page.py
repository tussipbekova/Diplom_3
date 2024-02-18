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

    @allure.step('Клик по крестику всплывающего окна')
    def click_to_close_button(self):
        self.click(close_button_locator)

    @allure.step('Достаем неактивный элемент в меню')
    def get_un_active_element(self):
        return self.get_element(un_active_element_locator)


    @allure.step('Получаем счетчик булок')
    def get_buns_counter(self):
        counter = self.get_text(ingredient_counter_link_locator)
        counter = int(counter)
        return counter

    @allure.step('Добавляем булку в заказ')
    def drag_and_drop_bun(self):
        source = self.wait_for_visibility(ingredient_counter_link_locator)
        target = self.wait_for_visibility(dragndrop_bun_target_locator)
        self.drag_and_drop(source, target)

    @allure.step('Добавляем соус в заказ')
    def drag_and_drop_sauce(self):
        self.scroll_to_sauce()
        source = self.wait_for_visibility(ingredient_3_link_locator)
        target = self.wait_for_visibility(dragndrop_bun_target_locator)
        self.drag_and_drop(source, target)

    @allure.step('Добавляем начинку в заказ')
    def drag_and_drop_filling(self):
        self.scroll_to_filling()
        source = self.wait_for_visibility(ingredient_7_link_locator)
        target = self.wait_for_visibility(dragndrop_bun_target_locator)
        self.drag_and_drop(source, target)

    @allure.step('Прокручиваем страницу к соусу')
    def scroll_to_sauce(self):
        # Прокручиваем страницу вниз
        sauce_element = self.scroll_to_element_by_locator(ingredient_3_link_locator)
        return sauce_element

    @allure.step('Прокручиваем страницу к начинке')
    def scroll_to_filling(self):
        filling_element = self.scroll_to_element_by_locator(ingredient_7_link_locator)
        return filling_element

    @allure.step('Кликаем кнопку Оформить заказ')
    def click_order_button(self):
        self.click(order_button_locator)

    @allure.step('Ждем, что появилось всплывающее окно с деталями заказа')
    def order_details_is_visible(self):
        return self.wait_for_visibility(oder_modal_opened_link_locator)

    @allure.step('Получаем номер заказа')
    def get_new_order_number(self):
        return self.wait_for_visibility(oder_modal_order_number_locator).text






