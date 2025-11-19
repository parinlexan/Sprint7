import pytest

from methods.courier_methods import CourierMethods

@pytest.fixture()
def create_courier():
    courier = CourierMethods()
    courier_data = courier.register_new_courier_and_return_login_password()
    yield courier_data