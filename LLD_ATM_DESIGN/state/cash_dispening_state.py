from .atm_state import AtmState
from .Enum_state import StateType
from ..custom_exception.exception import IllegalStateException
from .card_inject_state import CardInjectState
from ..db.db_accesor import DBAccesor
from ..card.card_manager_factory import CardManagerFactory
class CashDispensingState(AtmState):
    def __init__(self, atm):
        self.atm = atm

    def init(self):
        raise IllegalStateException("Invalid state")

    def cancel_transaction(self, trans_id):
        DBAccesor.cancel_transcation(trans_id)
        self.atm.change_state(CardInjectState(self.atm))
        return True

    def read_card(self, card_type, card_details):
        raise IllegalStateException("Invalid state")

    def read_withdrawal_details(self, card_type, card_details, trans_id, amount):
        raise IllegalStateException("Invalid state")

    def dispense_cash(self, trans_id):
        card_type = ""
        res = CardManagerFactory.get_card_manager(card_type).execute_withdrawal(trans_id)
        self.atm.change_state(CardInjectState(self.atm))
        return DBAccesor.mark_as_executed(trans_id)


    def inject_card(self):
        raise IllegalStateException("Invalid state")

    def get_state_name(self):
        return StateType.CASH_DISPENSE_STATE