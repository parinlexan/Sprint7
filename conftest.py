import pytest
import requests

from helpers import *
from methods.courier_methods import CourierMethods
from urls import *

@pytest.fixture()
def create_delete_courier():
    courier = CourierMethods()
    courier_data = courier.register_new_courier_and_return_login_password()
    yield courier_data
    courier.delete_courier()

@pytest.fixture()
def delete_courier():
    yield
    delete = CourierMethods()
    delete.delete_courier()
    store_login(login, password)
    login_payload = {
        "login": login,
        "password": password,
    }
    response = requests.post(f"{BASE_URL}{LOGIN_COURIER}", json=login_payload)
    assert response.status_code == 404