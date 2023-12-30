from food_delivery_system.data.food_item import FoodItem
from typing import List


class Menu:
    def __init__(self, food_item: List[FoodItem]):
        self.food_item = food_item
