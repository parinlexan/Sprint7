import allure
import requests

from conftest import *
from data import *
from urls import *
from helpers import *


class TestCreateCourier:

    @allure.title("/api/v1/courier -> 200 OK: все поля заполнены")
    @allure.description("Успешное создание курьера со всеми заполненными полями")
    def test_create_courier(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10),
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)

        assert response.status_code == 201 and response.json().get("ok") is True

    @allure.title("/api/v1/courier -> 200 OK: firstName = null")
    @allure.description("Успешное создание курьера без firstName (со всеми обязательными полями)")
    def test_create_courier_no_name(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)

        assert response.status_code == 201 and response.json().get("ok") is True

    @allure.title("/api/v1/courier -> 400 bad request: empty body")
    @allure.description("Ошибка при создании курьера с пустым телом запроса")
    def test_empty_body(self):
        payload = {}
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)

        assert response.status_code == 400 and COURIER_CREATE_DATA_ERROR == response.json().get("message")

    @allure.title("/api/v1/courier -> 400 bad request: password=null")
    @allure.description("Ошибка при создании курьера без password")
    def test_no_password(self):
        payload = {
            "login": generate_random_string(10),
            "firstName": generate_random_string(10),
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)

        assert response.status_code == 400 and COURIER_CREATE_DATA_ERROR == response.json().get("message")

    @allure.title("/api/v1/courier -> 400 bad request: login=null")
    @allure.description("Ошибка при создании курьера без login")
    def test_no_password(self):
        payload = {
            "firstName": generate_random_string(10),
            "password": generate_random_string(10),
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)

        assert response.status_code == 400 and COURIER_CREATE_DATA_ERROR == response.json().get("message")

    @allure.title("/api/v1/courier -> 409 conflict: создаем курьера дважды")
    @allure.description("Ошибка при создании уже существующего в системе курьера")
    def test_no_password(self, create_courier):
        payload = {
            "firstName": create_courier[2],
            "password": create_courier[1],
            "login": create_courier[0],
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)

        assert response.status_code == 409 and COURIER_EXISTS_ERROR == response.json().get("message")