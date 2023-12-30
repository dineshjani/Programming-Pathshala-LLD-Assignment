from food_item_filter import FoodItemFilter
from typing import List
from food_delivery_system.data.cuisine_type import CuisineType
from food_delivery_system.data.food_item import FoodItem
from restaurant_filter import RestaurantFilter
from food_delivery_system.data.restaurant import Restaurant


class CuisineTypeFilter(FoodItemFilter, RestaurantFilter):
    def __init__(self, cuisine_types: List[CuisineType]):
        self.cuisine_types = cuisine_types

    def filter_food_item(self, food_item: FoodItem):
        return food_item.cuisine_type in self.cuisine_types

    def filter_restaurant(self, restaurant: Restaurant):
        return any(
            cuisine in restaurant.cuisine_types for cuisine in self.cuisine_types
        )
