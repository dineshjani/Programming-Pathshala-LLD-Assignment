from abc import ABC,abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self):
        pass
    @abstractmethod
    def get_payable_amount(self):
        pass