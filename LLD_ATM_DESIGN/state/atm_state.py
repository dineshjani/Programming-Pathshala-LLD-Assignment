from abc import ABC, abstractmethod
from ..card.card_details import CardDetails

class AtmState(ABC):
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def cancel_transaction(self, trans_id):
        pass

    @abstractmethod
    def read_card(self, card_type, cardDetails:CardDetails):
        pass

    @abstractmethod
    def read_withdrawal_details(self, card_type, cardDetails:CardDetails, trans_id, amount):
        pass

    @abstractmethod
    def dispense_cash(self, trans_id):
        pass

    @abstractmethod
    def inject_card(self):
        pass

    @staticmethod
    def get_state_name(self):
        pass

