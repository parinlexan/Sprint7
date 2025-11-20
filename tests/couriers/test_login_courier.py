import allure
import pytest
import requests

from conftest import *
from data import *
from urls import *
from helpers import *


class TestLoginCourier:

    @allure.title("/api/v1/courier/login -> 200 OK: все поля заполнены")
    @allure.description("Успешный логин курьера в системе")
    def test_login_courier(self, create_delete_courier):
        payload = {
            "login": create_delete_courier[0],
            "password": create_delete_courier[1],
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}{LOGIN_COURIER}", json=payload)

        assert response.status_code == 200 and "id" in response.json()

    @allure.title("/api/v1/courier/login -> 400 bad request: login=null")
    @allure.description("Ошибка при попытке залогировать курьера в системе без логина")
    def test_login_courier_no_login(self, create_delete_courier):
        payload = {
            "password": create_delete_courier[1],
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}{LOGIN_COURIER}", json=payload)

        assert response.status_code == 400 and COURIER_LOGIN_DATA_ERROR == response.json().get("message")

    @allure.title("/api/v1/courier/login -> 400 bad request: password=null")
    @allure.description("Ошибка при попытке залогировать курьера в системе без пароля")
    def test_login_courier_no_password(self, create_delete_courier):
        payload = {
            "login": create_delete_courier[0],
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}{LOGIN_COURIER}", json=payload)

        assert response.status_code == 400 and COURIER_LOGIN_DATA_ERROR == response.json().get("message")

    @allure.title("/api/v1/courier/login -> 400 bad request: emptyBody")
    @allure.description("Ошибка при попытке залогировать курьера в системе без данных")
    def test_login_courier_no_body(self, create_delete_courier):
        payload = {}
        response = requests.post(f"{BASE_URL}{COURIERS_URL}{LOGIN_COURIER}", json=payload)

        assert response.status_code == 400 and COURIER_LOGIN_DATA_ERROR == response.json().get("message")

    @allure.title("/api/v1/courier/login -> 404 not found: password=random")
    @allure.description("Ошибка при попытке залогировать курьера со случайным паролем")
    def test_login_courier_random_password(self, create_delete_courier):
        payload = {
            "login": create_delete_courier[0],
            "password": generate_random_string(10),
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}{LOGIN_COURIER}", json=payload)

        assert response.status_code == 404 and COURIER_LOGIN_INCORRECT_ERROR == response.json().get("message")

    @allure.title("/api/v1/courier/login -> 404 not found: login=random")
    @allure.description("Ошибка при попытке залогировать курьера со случайным логином")
    def test_login_courier_random_login(self, create_delete_courier):
        payload = {
            "password": create_delete_courier[1],
            "login": generate_random_string(10),
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}{LOGIN_COURIER}", json=payload)

        assert response.status_code == 404 and COURIER_LOGIN_INCORRECT_ERROR == response.json().get("message")

    @allure.title("/api/v1/courier/login -> 404 not found: несуществующий курьер")
    @allure.description("Ошибка при попытке залогировать несуществующего курьера")
    def test_login_courier_random_login(self):
        payload = {
            "password": generate_random_string(10),
            "login": generate_random_string(10),
        }
        response = requests.post(f"{BASE_URL}{COURIERS_URL}{LOGIN_COURIER}", json=payload)

        assert response.status_code == 404 and COURIER_LOGIN_INCORRECT_ERROR == response.json().get("message")