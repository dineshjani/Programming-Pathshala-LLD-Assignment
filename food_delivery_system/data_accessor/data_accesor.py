from food_delivery_system.data.food_item import FoodItem
from food_delivery_system.data.user import User
from typing import List
from food_delivery_system.data.cart_item import CartItem


class DataAccessor:
    @staticmethod
    def get_food_items_with_name(food_item_name):
        return []

    @staticmethod
    def restaurant_with_name(restaurant_name):
        return []

    @staticmethod
    def add_item_to_cart(user: User, food_item: FoodItem):
        pass

    @staticmethod
    def get_user_cart(user: User):
        pass

    @staticmethod
    def delete_item_from_cart(user: User, food_item: FoodItem):
        pass

    @staticmethod
    def checkout_cart(user: User):
        pass

    @staticmethod
    def create_order(user_id, cart_items: List[CartItem]) -> str:
        pass

    @staticmethod
    def update_order_status(user_id, status):
        pass
