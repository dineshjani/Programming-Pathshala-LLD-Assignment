from .atm_state import AtmState
from .card_reading_state import CardReadingState
from ..custom_exception.exception import IllegalStateException
from ..db.db_accesor import DBAccesor
from .Enum_state import StateType
class ReadyState(AtmState):
    def __init__(self, atm):
        self.atm = atm

    def init(self):
        tid = DBAccesor.create_new_transcation(self.atm.machine_id)
        if tid ==0:
            raise RuntimeError("invalid transcation")
        self.atm.change_state(CardReadingState(self.atm))
        return tid


    def cancel_transaction(self, trans_id):
        raise IllegalStateException("Invalid state")


    def read_card(self, card_type, card_details):
        raise IllegalStateException("Invalid state")

    def read_withdrawal_details(self, card_type, card_details, trans_id, amount):
        raise IllegalStateException("Invalid state")

    def dispense_cash(self, trans_id):
        raise IllegalStateException("Invalid state")

    def inject_card(self):
        raise IllegalStateException("Invalid state")

    def get_state_name(self):
        return StateType.READY