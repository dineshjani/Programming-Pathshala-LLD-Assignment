from design_ecommerce_application.data.product import Product
from design_ecommerce_application.data.product_copy import ProductCopy
from design_ecommerce_application.data.cart import Cart
from design_ecommerce_application.data.user import User
from design_ecommerce_application.data.order import Order
from typing import List


class DbAccessor:
    def __init__(self):
        pass

    def get_prodcut_by_name(self, product_name) -> List[Product]:
        pass

    def get_product_copy_by_id(self, id) -> ProductCopy:
        pass

    def get_cart_by_user(self, user: User) -> Cart:
        pass

    def check_out_cart(self, user: User, order: Order):
        pass

    def persist_cart(self, user, cart: Cart):
        pass

    def get_order_by_order_id(self, order_id) -> Order:
        pass
