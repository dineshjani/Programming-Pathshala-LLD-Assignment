from design_ecommerce_application.data.cart import Cart
from design_ecommerce_application.db_accessor.db_accessor import DbAccessor
from design_ecommerce_application.data.product_copy import ProductCopy
from design_ecommerce_application.data.user import User
from design_ecommerce_application.data.order import Order


class CartManager:
    def get_cart(self, user) -> Cart:
        return DbAccessor.get_cart_by_user(user)

    def add_to_cart(self, user: User, product_copy: ProductCopy):
        if product_copy.is_sold:
            raise RuntimeError("Cannot add already sold product to cart")
        cart: Cart = self.get_cart(user)
        cart.add(product_copy)
        DbAccessor.persist_cart(user, cart)

    def remove_from_cart(self, user, product_copy):
        cart: Cart = self.get_cart(user)
        cart.remove(product_copy)
        DbAccessor.persist_cart(user, cart)

    def checkout_cart(self, user: User, order: Order):
        DbAccessor.check_out_cart(user, order)
