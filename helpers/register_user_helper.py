import allure
import random
import string

from helpers.requests_helper import HelpersOnRequests as hr

class RegisterUserHelper:

    @staticmethod
    @allure.step('Генерируем данные нового пользователя: email, password, name')
    def generate_random_user_data():
        email = RegisterUserHelper.generate_random_string(10) + '@yandex.ru'
        password = RegisterUserHelper.generate_random_string(10)
        name = RegisterUserHelper.generate_random_string(10)

        payload = {
            'email': email,
            'password': password,
            'name': name
        }

        return payload

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    @allure.step('Отправляем запрос на создание нового пользователя')
    def try_to_create_user(user_data):
        response = hr.request_on_create_user(user_data)
        return response

    @staticmethod
    @allure.step('Удаляем пользователя')
    def try_to_delete_user(auth_token):
        headers = {'Authorization': auth_token}
        response = hr.request_on_delete_user(headers)
        return response

