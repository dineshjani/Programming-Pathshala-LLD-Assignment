from food_delivery_system.Permission.pertmission import Permission
from food_delivery_system.data.order import Order
from food_delivery_system.data.order_status import OrderStatus


class UpdateOrderPermission(Permission):
    def __init__(self, user, order: Order, status: OrderStatus):
        self.user = user
        self.order = order
        self.status = status

    def is_permitted(self):
        pass
