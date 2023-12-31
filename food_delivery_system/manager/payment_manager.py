from abc import ABC, abstractmethod
from food_delivery_system.data.payment_response import PaymentResponse


class PaymentManager(ABC):
    @abstractmethod
    def execute_payment(self) -> PaymentResponse:
        pass
