from food_delivery_system.data.meal_type import MealType
from food_delivery_system.data.cuisine_type import CuisineType
from food_delivery_system.data.star_rating import StarRating
from food_delivery_system.data.restaurant import Restaurant
from food_delivery_system.filter.meal_type_filter import MealTypeFilter
from food_delivery_system.filter.cuisine_type_fllter import CuisineTypeFilter
from food_delivery_system.filter.star_rating_filter import StarRatingFilter
from food_delivery_system.searchers.restaurant_searcher import RestaurantSearcher
from typing import List


class RestaurantSearcherApi:
    @staticmethod
    def search_restaurant(
        restaurant_name,
        meal_type: MealType,
        cuisines: List[CuisineType],
        ratings: List[StarRating],
    ) -> List[Restaurant]:
        filters = []
        if meal_type is not None:
            filters.append(MealTypeFilter(meal_type))
        if cuisines is not None:
            filters.append(CuisineTypeFilter(cuisines))
        if ratings is not None:
            filters.append(StarRatingFilter(ratings))
        return RestaurantSearcher.search(restaurant_name, filters)
