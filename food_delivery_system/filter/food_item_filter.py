from abc import ABC, abstractmethod
from food_delivery_system.data.food_item import FoodItem


class FoodItemFilter(ABC):
    @abstractmethod
    def filter_food_item(self, food_item: FoodItem):
        pass
