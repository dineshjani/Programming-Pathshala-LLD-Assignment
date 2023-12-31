from food_delivery_system.Permission.pertmission import Permission
from food_delivery_system.data.user import User


class CheckoutCartPermission(Permission):
    def __init__(self, user: User):
        self.user = user

    def is_permitted(self):
        pass
