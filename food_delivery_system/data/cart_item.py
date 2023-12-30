from typing import List
from food_item import FoodItem


class CartItem:
    def __init__(self, food_item: FoodItem, quantity):
        self.food_item = food_item
        self.quantity = quantity
