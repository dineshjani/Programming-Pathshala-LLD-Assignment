from payment_manager import PaymentManager
from food_delivery_system.data.payment_response import PaymentResponse


class CardBasedPymentManager(PaymentManager):
    def __init__(self, bank_name, card_number, pin, amount):
        self.bank_name = bank_name
        self.card_number = card_number
        self.pin = pin
        self.amount = amount

    def execute_payment(self) -> PaymentResponse:
        pass
