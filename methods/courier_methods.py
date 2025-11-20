import allure
import requests

from helpers import *
from urls import *


class CourierMethods:

    @allure.step("Создать курьера")
    def register_new_courier_and_return_login_password(self):
        login_pass = []

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass

    @allure.step("Логин курьера в системе")
    def login_courier(self):
        login, password = get_login()

        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f'{BASE_URL}{LOGIN_COURIER}', data=payload)

        return response.json()

    @allure.step("Удаление курьера")
    def delete_courier(self):
        login_pass = self.login_courier()
        courier_id = login_pass.get('id')
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}/:{courier_id}')

        if response.status_code == 200:
            return response.json()
        else:
            return {"status_code": response.status_code, "message": response.text}
