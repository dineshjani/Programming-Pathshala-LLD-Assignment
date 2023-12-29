from payment_processor import PaymentProcessor
from card_details import CardDetails


class CardPaymentProcessor(PaymentProcessor):

    def __init__(self, amount, card_details:CardDetails):
        self.amount = amount
        self.card_details = card_details

    @staticmethod
    def execute_payment():
        pass
