from food_delivery_system.data.business_hours import BusinessHours
from food_delivery_system.data.cuisine_type import CuisineType
from typing import List


class Restaurant:
    def __init__(
        self,
        id,
        name,
        description,
        business_hours: BusinessHours,
        meal_type,
        cuisine_types: List[CuisineType],
        star_rating,
        menu,
        address,
    ):
        self.cuisine_types = cuisine_types
        self.id = id
        self.name = name
        self.description = description
        self.business_hours = business_hours
        self.meal_type = meal_type
        self.star_rating = star_rating
        self.menu = menu
        self.address = address
