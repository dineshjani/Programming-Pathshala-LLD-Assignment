from food_delivery_system.data.payment_response import PaymentResponse
from payment_manager import PaymentManager


class NetBankingManager(PaymentManager):
    def __init__(self, bank_name, user_name, pin, password, amount):
        # can use builder pattern here take arguments as data class
        self.bank_name = bank_name
        self.user_name = user_name
        self.pin = pin
        self.password = password
        self.amount = amount

    def execute_payment(self) -> PaymentResponse:
        pass
