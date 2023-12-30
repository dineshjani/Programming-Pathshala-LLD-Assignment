from food_item_filter import FoodItemFilter
from food_delivery_system.data.food_item import FoodItem
from food_delivery_system.data.restaurant import Restaurant
from food_delivery_system.data.meal_type import MealType


class MealTypeFilter(FoodItemFilter):
    def __init__(self, meal_type: MealType):
        self.meal_type = meal_type

    def filter_food_item(self, food_item: FoodItem):
        return food_item.meal_type == self.meal_type

    def filter_restaurant(self, restaurant: Restaurant):
        return restaurant.meal_type in self.meal_type
