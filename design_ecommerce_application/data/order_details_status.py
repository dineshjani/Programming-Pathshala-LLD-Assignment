from design_ecommerce_application.data.order_status import OrderStatus


class OrderDetailsStatus:
    def __init__(self, order_status: OrderStatus, description: str):
        self.order_status = order_status
        self.description = description
