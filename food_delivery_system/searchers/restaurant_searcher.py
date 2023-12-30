from typing import List
from food_delivery_system.data.restaurant import Restaurant
from food_delivery_system.filter.restaurant_filter import RestaurantFilter
from food_delivery_system.data_accessor.data_accesor import DataAccessor


class RestaurantSearcher:
    def search(restaurant_name, filters: List[RestaurantFilter]) -> List[Restaurant]:
        if restaurant_name == "" or restaurant_name is None:
            raise RuntimeError("invalid restaurant name")

        restaurants: List[Restaurant] = DataAccessor.restaurant_with_name(
            restaurant_name
        )
        for _filter in filters:
            filter_restaurants = []
            for restaurant in restaurants:
                if _filter.filter_restaurant(restaurant):
                    filter_restaurants.append(restaurant)
                restaurants = filter_restaurants
        return restaurants

    def get_restaurant_by_id(id) -> Restaurant:
        pass
