from food_delivery_system.data.user import User
from food_delivery_system.data.cart_item import CartItem
from food_delivery_system.data.food_item import FoodItem
from food_delivery_system.factory.permission_factory import PermissionFactory
from typing import List
from food_delivery_system.data_accessor.data_accesor import DataAccessor


class CartManager:
    @staticmethod
    def get_user_cart(user: User) -> List[CartItem]:
        resp = DataAccessor.get_user_cart(user)
        # convert resp as wanted format
        return resp

    @staticmethod
    def add_item_to_cart(user: User, food_item: FoodItem):
        # here instead of craete an permission object we should call factory class
        # interface segragation principal
        # high class only depend on factory class
        is_permitted = PermissionFactory.get_add_to_cart_permission(
            user, food_item
        ).is_permitted()
        if not is_permitted:
            raise RuntimeError("Not permitted for add-to-cart operation")
        if not CartManager.is_food_item_from_same_restaurant(user, food_item):
            raise RuntimeError("food-item from different rest-id")
        DataAccessor.add_item_to_cart(user, food_item)

    @staticmethod
    def is_food_item_from_same_restaurant(user: User, food_item: FoodItem):
        cart_items: List[CartItem] = CartManager.get_user_cart(user)
        if len(cart_items) == 0:
            return True
        restaurant_id = cart_items[0].food_item.restaurant_id
        return restaurant_id == food_item.restaurant_id

    @staticmethod
    def delete_item_from_cart(user: User, food_item: FoodItem):
        is_permitted = PermissionFactory.get_delete_item_from_cart_permission(
            user, food_item
        ).is_permitted()
        if not is_permitted:
            raise RuntimeError("Not permitted for add-to-cart operation")
        DataAccessor.delete_item_from_cart(user, food_item)

    @staticmethod
    def checkout_user_cart(user: User):
        pass


# write need to permission for do operation
