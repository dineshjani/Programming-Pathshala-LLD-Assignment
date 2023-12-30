from food_delivery_system.manager.user_manager import UserManager
from food_delivery_system.searchers.food_item_searcher import FoodItemSearcher
from food_delivery_system.manager.cart_manager import CartManager
from food_delivery_system.data.user import User
from food_delivery_system.data.food_item import FoodItem


class AddToCardApi:
    @staticmethod
    def add_to_cart(user_token, food_item_id):
        if user_token is None or len(user_token) == 0:
            raise RuntimeWarning("Invalid user-token")
        user: User = UserManager.get_user_by_token(user_token)
        if user is None:
            raise RuntimeError("User-id Not found")
        food_item: FoodItem = FoodItemSearcher.get_food_by_id(food_item_id)
        if food_item is None:
            raise RuntimeError("food-item Not found")
        CartManager.add_item_to_cart(user, food_item)
