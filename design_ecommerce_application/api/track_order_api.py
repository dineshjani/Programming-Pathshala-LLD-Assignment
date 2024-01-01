from design_ecommerce_application.data.order_details_status import OrderDetailsStatus
from design_ecommerce_application.data.user import User
from design_ecommerce_application.db_accessor.db_accessor import DbAccessor
from design_ecommerce_application.data.order import Order
from design_ecommerce_application.permission.permission_factory import PermissionFactory
from design_ecommerce_application.permission.permission import Permission


class TrackOrderApi:
    def track_order(self, order_id, user: User):
        order: Order = DbAccessor().get_order_by_order_id(order_id)
        if order is None:
            raise RuntimeError("Order not found")
        permission: Permission = PermissionFactory.track_order_permission(user)
        if not permission.is_permitted():
            raise RuntimeError("Permission is denied to track order")
        return order.get_order_status_details()
