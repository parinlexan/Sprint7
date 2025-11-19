import allure
import requests

from conftest import *
from data import *
from urls import *


class TestOrderCreate:

    @allure.title("/api/v1/orders -> 200 ok: успешное создание заказа")
    @allure.description("Успешное создание заказа без выбора цвета, с черным, серым, черным/серым цветами")
    @pytest.mark.parametrize("color", [[], ["BLACK"], ["GREY"], ["BLACK", "GREY"]])
    def test_order_create(self, color):
        payload = order_data.copy()
        payload["color"] = color
        response = requests.post(f"{BASE_URL}{ORDERS_URL}", json=payload)

        assert response.status_code == 201 and "track" in response.json()