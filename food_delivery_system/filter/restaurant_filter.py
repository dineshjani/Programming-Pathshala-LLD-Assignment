from abc import ABC, abstractmethod


class RestaurantFilter(ABC):
    @abstractmethod
    def filter_restaurant(self, restaurant_name):
        pass
