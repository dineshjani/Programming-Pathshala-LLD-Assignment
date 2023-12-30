from .atm_state import AtmState
from .Enum_state import StateType
from ..custom_exception.exception import IllegalStateException
from .ready_state import ReadyState


class CardInjectState(AtmState):
    def __init__(self, atm):
        self.atm = atm

    def init(self):
        raise IllegalStateException("invalid state")

    def cancel_transaction(self, trans_id):
        raise IllegalStateException("invalid state")

    def read_card(self, card_type, card_details):
        raise IllegalStateException("invalid state")

    def read_withdrawal_details(self, card_type, card_details, trans_id, amount):
        raise IllegalStateException("invalid state")

    def dispense_cash(self, trans_id):
        raise IllegalStateException("invalid state")

    def inject_card(self):
        self.atm.change_state(ReadyState(self.atm))

    def get_state_name(self):
        return StateType.CARD_INJECT_STATE
