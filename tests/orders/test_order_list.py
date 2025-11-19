import allure
import requests

from urls import *


class TestOrderList:

    @allure.title("/api/v1/orders -> 200 ok: успешное получение списка заказов")
    def test_order_list(self):
        response = requests.get(f"{BASE_URL}{ORDERS_URL}")

        assert response.status_code == 200 and "orders" in response.json()