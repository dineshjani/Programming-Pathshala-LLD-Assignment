from enum import Enum


class OrderStatus(Enum):
    ORDER_PLACED = 1
    COOKING = 2
    READY_FOR_DELIVERY = 3
    OUT_FOR_DELIVERY = 4
    DELIVERED = 5
    CANCELLED = 6
