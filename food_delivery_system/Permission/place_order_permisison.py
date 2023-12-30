from food_delivery_system.Permission.pertmission import Permission


class PlaceOrderPermission(Permission):
    def __init__(self, user):
        self.user = user

    def is_permitted(self):
        pass
