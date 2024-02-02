import time

import allure
import pytest

from conftest import driver
from pages.feed_page import FeedPage
from pages.main_page import MainPage


class TestCheckingMainFunction:

    @allure.title('Проверка основного функционала')
    @allure.description('Проверка кнопок Конструктор, Лента заказов, клик по ингредиенту и оформление заказа')
    def test_click_to_constructor(self, driver):
        main_page = MainPage(driver)

        # ожидаем появления на странице заголовка Соберите бургер
        main_page.wait_for_load_home_page()

        # кликаем по кнопке Конструктор
        main_page.click_to_constructor_button()

        # ожидаем появления на странице заголовка Соберите бургер
        main_page.wait_for_load_home_page()

        expected_url = "https://stellarburgers.nomoreparties.site/"

        assert expected_url == driver.current_url

    def test_click_to_ordered_feed(self,driver):
        main_page = MainPage(driver)

        # ожидаем появления на странице заголовка Соберите бургер
        main_page.wait_for_load_home_page()

        # кликаем по кнопке Лента заказов
        main_page.click_to_ordered_feed()

        feed_page = FeedPage(driver)

        # ожидаем появления на странице заголовка Лента заказов
        feed_page.wait_for_load_feed_page()

        expected_url = "https://stellarburgers.nomoreparties.site/feed"

        assert expected_url == driver.current_url

    def test_click_to_ingredient(self,driver):
        main_page = MainPage(driver)

        # ожидаем появления на странице заголовка Соберите бургер
        main_page.wait_for_load_home_page()

        # кликаем по ингредиенту
        main_page.click_to_ingredient()

        active_field = main_page.get_pop_up_window_module()

        assert active_field != None

    #def test_click_close_pop_up_window(self,driver):







