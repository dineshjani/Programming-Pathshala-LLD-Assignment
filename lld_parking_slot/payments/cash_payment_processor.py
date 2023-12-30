from payment_processor import PaymentProcessor


class CashPaymentProcessor(PaymentProcessor):
    def __init__(self, amount):
        self.amount = amount

    @staticmethod
    def execute_payment():
        pass
