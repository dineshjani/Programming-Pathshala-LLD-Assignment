from typing import List
from food_delivery_system.filter.food_item_filter import FoodItemFilter
from food_delivery_system.data.food_item import FoodItem
from food_delivery_system.data_accessor.data_accesor import DataAccessor


class FoodItemSearcher:
    """
    Now this class have single responsibility and new filter comes then its will not change
    its following Single Responsibility and OPen closed Principal
    """

    def search(food_item_name, filters: List[FoodItemFilter]) -> List[FoodItem]:
        if food_item_name == "" or food_item_name is None:
            raise RuntimeError("invalid food-Item")

        food_items: List[FoodItem] = DataAccessor.get_food_items_with_name(
            food_item_name
        )
        for _filter in filters:
            filter_food_item = []
            for food_item in food_items:
                if _filter.filter_food_item(food_item):
                    filter_food_item.append(food_item)
                food_items = filter_food_item
        return food_items

    def get_food_by_id(id) -> FoodItem:
        pass
