from payment_staus import PaymentStatus


class PaymentResponse:
    def __init__(self, amount, id, status: PaymentStatus):
        self.amount = amount
        self.id = id
        self.status = status
