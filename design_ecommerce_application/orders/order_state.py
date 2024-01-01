from abc import ABC, abstractmethod
from design_ecommerce_application.data.transit_details import TransitDetails
from design_ecommerce_application.data.delivery_details import DeliveryDetails
from design_ecommerce_application.data.pickup_details import PickupDetails
from design_ecommerce_application.data.order_details_status import OrderDetailsStatus

o


class OrderState(ABC):
    @abstractmethod
    def schedule_pickup(self, pickup_details: PickupDetails):
        pass

    @abstractmethod
    def pick_up(self):
        pass

    @abstractmethod
    def end_transit(self, transit_details: TransitDetails):
        pass

    @abstractmethod
    def schedule_delivery(self, delivery_details: DeliveryDetails):
        pass

    @abstractmethod
    def deliver(self):
        pass

    @abstractmethod
    def cancel(self):
        pass

    @abstractmethod
    def get_status(self) -> OrderDetailsStatus:
        pass
