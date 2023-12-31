from typing import List
from food_delivery_system.data.cart_item import CartItem
from food_delivery_system.data.data_access_result import DataAccessResult


class DataAccessObjectConverter:
    @staticmethod
    def convert_to_cart_items(result: DataAccessResult) -> List[CartItem]:
        pass
