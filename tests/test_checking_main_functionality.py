import allure

from conftest import driver
from pages.feed_page import FeedPage
from pages.main_page import MainPage


class TestCheckingMainFunction:

    @allure.title('Проверка основного функционала')
    @allure.description('Проверка перехода по  кнопке Конструктор')
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

    @allure.description('Проверка перехода по  кнопке Лента заказов')
    def test_click_to_ordered_feed(self, driver):
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

    @allure.description('Проверка клика по ингредиенту')
    def test_click_to_ingredient(self, driver):
        main_page = MainPage(driver)

        # ожидаем появления на странице заголовка Соберите бургер
        main_page.wait_for_load_home_page()

        # кликаем по ингредиенту
        main_page.click_to_ingredient()

        active_field = main_page.get_pop_up_window_module()

        assert active_field != None

    @allure.description('Проверка оформление заказа')
    def test_click_close_pop_up_window(self, driver):
        main_page = MainPage(driver)

        # ожидаем появления на странице заголовка Соберите бургер
        main_page.wait_for_load_home_page()

        # кликаем по ингредиенту
        main_page.click_to_ingredient()

        # кликаем по крестику во всплывающемся окне
        main_page.click_to_close_button()

        un_active_element = main_page.get_un_active_element()

        assert un_active_element != None

    @allure.description('Проверка, при добавлении ингредиента в заказ счётчик этого ингрeдиента увеличивается')
    def test_append_ingredient_to_order(self, driver):
        main_page = MainPage(driver)

        # ожидаем появления на странице заголовка Соберите бургер
        main_page.wait_for_load_home_page()

        # получаем значение счетчика До
        counter_before = main_page.get_buns_counter()
        # Перемещаем булку в бургер
        main_page.drag_and_drop_bun()
        # получаем значение счетчика после добавления ингредиента
        counter_after = main_page.get_buns_counter()

        # проверяем, что счетчик ингредиента увеличивается
        assert counter_after > counter_before

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    def test_make_order_by_login_user(self, driver, create_new_user, login_new_user):

        # открываем Главную страницу
        main_page = MainPage(driver)

        # ожидаем появления на странице заголовка Соберите бургер
        main_page.wait_for_load_home_page()
        # Перемещаем булку в бургер
        main_page.drag_and_drop_bun()
        # Добавляем соус в заказ
        main_page.drag_and_drop_sauce()
        # Добавляем начинку в заказ
        main_page.drag_and_drop_filling()
        # кликаем кнопку Оформить заказ
        main_page.click_order_button()

        # проверяем, что появилось модальное окно с деталями заказа
        assert main_page.order_details_is_visible()



