from food_delivery_system.manager.user_manager import UserManager
from food_delivery_system.manager.order_manager import OrderManager
from food_delivery_system.data.user import User
from food_delivery_system.data.order import Order
from food_delivery_system.data.order_status import OrderStatus


class UpdateOrderApi:
    @staticmethod
    def update_order_api(order_id, order_status, user_token):
        if user_token is None or len(user_token) == 0:
            raise RuntimeWarning("Invalid user-token")
        user: User = UserManager.get_user_by_token(user_token)
        order: Order = OrderManager().get_order(order_id)
        if order_status == OrderStatus.COOKING:
            OrderManager.set_order_to_cooking(user, order)
        elif order_status == OrderStatus.READY_FOR_DELIVERY:
            OrderManager.set_order_to_ready_for_delivery(user, order)
