from typing import List
from cart_item import CartItem
from order_status import OrderStatus


class Order:
    def __init__(
        self, cart_items: List[CartItem], order_id, user_id, order_status: OrderStatus
    ):
        self.cart_items = cart_items
        self.order_id = order_id
        self.user_id = user_id
        self.order_status = order_status
