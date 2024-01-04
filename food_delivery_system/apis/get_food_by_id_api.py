from food_delivery_system.searchers.food_item_searcher import FoodItemSearcher


class GetFoodById:
    @staticmethod
    def get_food_by_id_api(id):
        return FoodItemSearcher.get_food_by_id(id)
