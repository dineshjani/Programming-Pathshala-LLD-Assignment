class FoodItem:
    def __init__(
        self,
        id,
        name,
        description,
        price_inr,
        meal_type,
        cuisine_type,
        star_rating,
        restaurant_id,
        is_available,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.price_inr = price_inr
        self.cuisine_type = cuisine_type
        self.star_rating = star_rating
        self.restaurant_id = restaurant_id
        self.meal_type = meal_type
        self.is_available = is_available
