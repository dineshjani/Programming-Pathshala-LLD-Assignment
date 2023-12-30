from food_delivery_system.Permission.pertmission import Permission
from food_delivery_system.data.food_item import FoodItem
from food_delivery_system.data.user import User
from food_delivery_system.data.restaurant import Restaurant
from food_delivery_system.manager.delivery_manager import DeliveryManager
from food_delivery_system.searchers.restaurant_searcher import RestaurantSearcher


class AddToCartPermission(Permission):
    def __init__(self, user, food_item: FoodItem):
        self.user: User = user
        self.food_item = food_item
        self.delivery_manager = DeliveryManager()

    def is_permitted(self):
        if not self.food_item.is_available:
            return False
        restaurant: Restaurant = RestaurantSearcher.get_restaurant_by_id(
            self.food_item.restaurant_id
        )
        return self.delivery_manager.is_delivery_possible(
            restaurant.address, self.user.address
        )
