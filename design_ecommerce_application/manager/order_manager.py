from design_ecommerce_application.payment.payment_processor import PaymentProcessor
from design_ecommerce_application.data.address import Address
from design_ecommerce_application.data.order import Order
from design_ecommerce_application.data.cart import Cart
from design_ecommerce_application.manager.cart_manager import CartManager


class OrderManager:
    def __init__(self):
        pass

    def place_order(
        self,
        user,
        payment_processor: PaymentProcessor,
        shipping_address: Address,
        billing_address: Address,
    ) -> Order:
        cart: Cart = CartManager.get_cart(user)
        if cart.get_cart_amount() != payment_processor.get_payable_amount():
            raise RuntimeError("Invalid amount")
        if not payment_processor.process_payment():
            raise RuntimeError("Payment failed")
        order: Order = Order(
            self.get_order_id(), cart, shipping_address, billing_address
        )
        CartManager.checkout_cart(user, order)
        return order

    def get_order_id(self):
        return "1111"
