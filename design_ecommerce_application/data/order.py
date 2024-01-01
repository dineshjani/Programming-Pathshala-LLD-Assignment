from design_ecommerce_application.data.address import Address
from design_ecommerce_application.data.cart import Cart
from design_ecommerce_application.orders.order_state import OrderState
from design_ecommerce_application.data.pickup_details import PickupDetails
from design_ecommerce_application.data.transit_details import TransitDetails
from design_ecommerce_application.data.delivery_details import DeliveryDetails


class Order:
    def __init__(
        self, id: str, cart: Cart, shipping_address: Address, billings_address: Address
    ):
        self.id = id
        self.cart = cart
        self.shipping_address = shipping_address
        self.billings_address = billings_address
        # we can fetch here current state from db regarding id status

    def set_order_state(self, order_state: OrderState):
        self.order_state = order_state

    def get_order_status(self):
        return self.order_state

    def schedule_pickup(self, pickup_details: PickupDetails):
        self.order_state.schedule_pickup(pickup_details)

    def pick_up(self):
        self.order_state.pick_up()

    def end_transit(self, transit_details: TransitDetails):
        self.order_state.end_transit(transit_details)

    def schedule_delivery(self, delivery_details: DeliveryDetails):
        self.order_state.schedule_delivery(delivery_details)

    def deliver(self):
        self.order_state.deliver()

    def cancel(self):
        self.order_state.cancel()

    def get_order_status_details(self):
        return self.order_state.get_status()
