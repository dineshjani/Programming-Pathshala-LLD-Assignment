from order_state import OrderState
from design_ecommerce_application.data.transit_details import TransitDetails
from design_ecommerce_application.data.delivery_details import DeliveryDetails
from design_ecommerce_application.data.pickup_details import PickupDetails
from design_ecommerce_application.data.order_details_status import OrderDetailsStatus


class OrderPlacedState(OrderState):
    def schedule_pickup(self, pickup_details: PickupDetails):
        pass

    def pick_up(self):
        pass

    def end_transit(self, transit_details: TransitDetails):
        pass

    def schedule_delivery(self, delivery_details: DeliveryDetails):
        pass

    def deliver(self):
        pass

    def cancel(self):
        pass

    def get_status(self) -> OrderDetailsStatus:
        pass
