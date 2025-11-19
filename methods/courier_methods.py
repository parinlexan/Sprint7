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