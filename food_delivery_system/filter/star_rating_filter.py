from food_item_filter import FoodItemFilter
from restaurant_filter import RestaurantFilter
from food_delivery_system.data.food_item import FoodItem
from food_delivery_system.data.restaurant import Restaurant
from food_delivery_system.data.star_rating import StarRating
from typing import List


class StarRatingFilter(FoodItemFilter, RestaurantFilter):
    def __init__(self, star_ratings: List[StarRating]):
        self.star_ratings = star_ratings

    def filter_food_item(self, food_item: FoodItem):
        return food_item.star_rating in self.star_ratings

    def filter_restaurant(self, restaurant: Restaurant):
        return restaurant.star_rating in self.star_ratings
