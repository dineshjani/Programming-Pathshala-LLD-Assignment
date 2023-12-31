from typing import Dict
from food_delivery_system.data.order import Order
from food_delivery_system.data.user import User
from food_delivery_system.manager.user_manager import UserManager
from food_delivery_system.factory.payment_factory import PaymentFactory
from food_delivery_system.manager.payment_manager import PaymentManager
from food_delivery_system.data.payment_response import PaymentResponse
from food_delivery_system.data.payment_staus import PaymentStatus
from food_delivery_system.manager.order_manager import OrderManager


class PlaceOrder:
    """
    This class only have to know about payment_manager which is abstract thing and not know about implemention things
    """

    @staticmethod
    def place_order(
        user_token, payment_info: Dict[str, str], payment_mode: str
    ) -> Order:
        if user_token is None or len(user_token) == 0:
            raise RuntimeWarning("Invalid user-token")
        user: User = UserManager.get_user_by_token(user_token)
        if user is None:
            raise RuntimeError("User-id Not found")
        payment_manager: PaymentManager = PaymentFactory.get_payment_manager(
            payment_mode, payment_info
        )
        payment_response: PaymentResponse = payment_manager.execute_payment()
        if payment_response is None or payment_response.status == PaymentStatus.FAILURE:
            raise RuntimeError("Payment is Failed")
        return OrderManager().place_order(user)
