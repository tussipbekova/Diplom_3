import allure
import requests

from data.data import *


class HelpersOnRequests:

    @staticmethod
    @allure.step('Отправляем API-запрос на создание пользователя')
    def request_on_create_user(payload):
        request_url = f'{URL}{ENDPOINT_CREATE_USER}'
        response = requests.post(f'{request_url}', json=payload)
        return response

    @staticmethod
    @allure.step('Отправляем API-запрос на удаление пользователя')
    def request_on_delete_user(headers):
        request_url = f'{URL}{ENDPOINT_DELETE_USER}'
        response = requests.delete(f'{request_url}', headers=headers)
        return response

