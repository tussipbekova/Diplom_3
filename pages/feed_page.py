import allure

from locators.feed_locators import feed_page_title_locator
from locators.main_locators import *
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Ожидание загрузки заголовка Лента заказов')
    def wait_for_load_feed_page(self):
        self.wait_for_visibility(feed_page_title_locator)

