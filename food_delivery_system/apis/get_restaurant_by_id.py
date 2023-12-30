from food_delivery_system.searchers.restaurant_searcher import RestaurantSearcher


class GetRestaurantById:
    @staticmethod
    def get_restaurant_by_id_api(id):
        return RestaurantSearcher.get_restaurant_by_id(id)
