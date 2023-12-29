from abc import ABC,abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    @staticmethod
    def execute_payment():
        pass
