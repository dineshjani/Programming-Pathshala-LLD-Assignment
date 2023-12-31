from food_delivery_system.data_accessor.data_accesor import DataAccessor
from food_delivery_system.data.order import Order
from food_delivery_system.data.user import User
from food_delivery_system.data.cart_item import CartItem
from food_delivery_system.data.order_status import OrderStatus
from food_delivery_system.factory.permission_factory import PermissionFactory
from cart_manager import CartManager
from typing import List


class OrderManager:
    def __init__(self):
        pass

    def place_order(self, user: User) -> Order:
        is_permitted = PermissionFactory.get_add_to_cart_permission(user).is_permitted()
        if not is_permitted:
            raise RuntimeError("Not permitted for add-to-cart operation")
        cart_items: List[CartItem] = CartManager.get_user_cart(user)
        order_id = DataAccessor.create_order(user, cart_items)
        CartManager.checkout_user_cart(user)
        return Order(cart_items, order_id, user.user_id, OrderStatus.ORDER_PLACED)

    def get_order(self, order_id) -> Order:
        pass

    def get_orders(self, user: User) -> List[Order]:
        pass

    def set_order_to_cooking(self, user, order: Order):
        is_permitted = PermissionFactory.get_update_order_permision(user).is_permitted()
        if not is_permitted:
            raise RuntimeError("Not permitted for update operation")
        if order.order_status != OrderStatus.ORDER_PLACED:
            raise RuntimeError("Cannot update order which is not placed")
        DataAccessor.update_order_status(user.user_id, order.order_status)

    def set_order_to_ready_for_delivery(self, user, order: Order):
        is_permitted = PermissionFactory.get_update_order_permision(user).is_permitted()
        if not is_permitted:
            raise RuntimeError("Not permitted for update operation")
        if order.order_status != OrderStatus.COOKING:
            raise RuntimeError(
                "Cannot update order  order to Ready-for-delivery which is not cooking"
            )
        DataAccessor.update_order_status(user.user_id, order.order_status)

    def set_order_to_out_for_delivery(self, user, order: Order):
        is_permitted = PermissionFactory.get_update_order_permision(user).is_permitted()
        if not is_permitted:
            raise RuntimeError("Not permitted for update operation")
        if order.order_status != OrderStatus.READY_FOR_DELIVERY:
            raise RuntimeError(
                "Cannot update order to out-of-delivery which is not ready for delivered"
            )
        DataAccessor.update_order_status(user.user_id, order.order_status)

    def set_order_to_cancelled(self, user, order: Order):
        is_permitted = PermissionFactory.get_update_order_permision(user).is_permitted()
        if not is_permitted:
            raise RuntimeError("Not permitted for update operation")
        if order.order_status != OrderStatus.READY_FOR_DELIVERY:
            raise RuntimeError(
                "Cannot update order to out-of-delivery which is not ready for delivered"
            )
        DataAccessor.update_order_status(user.user_id, order.order_status)


# need to craete order table
# Todo
# Here we can do state design pattern for changing status
