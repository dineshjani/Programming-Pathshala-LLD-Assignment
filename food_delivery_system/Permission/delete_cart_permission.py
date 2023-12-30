from food_delivery_system.Permission.pertmission import Permission


class DeleteCartPermission(Permission):
    def __init__(self, user, food_item):
        self.user = user
        self.food_item = food_item

    def is_permitted(self):
        pass
