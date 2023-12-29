from card_payment_processor import CardPaymentProcessor
from cash_payment_processor import CashPaymentProcessor
class PaymentProcessorFactory:
    @staticmethod
    def get_card_payment_processor(amount, card_details):
        return CardPaymentProcessor(amount, card_details)

    @staticmethod
    def get_cash_payment_processor(amount):
        return CashPaymentProcessor(amount)