from .atm_state import AtmState
from .Enum_state import StateType
from ..db.db_accesor import DBAccesor
from .card_inject_state import CardInjectState
from .cash_dispening_state import CashDispensingState
from ..custom_exception.exception import IllegalStateException
from ..card.card_manager_factory import CardManagerFactory
from ..card.transcation_status import TranscationStatus
class WithdrawlReadingState(AtmState):
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
        result = CardManagerFactory.get_card_manager(card_type).validate_withdrawal(trans_id, amount)
        if result:
            self.atm.change_state(CashDispensingState(self.atm))
            DBAccesor.persist_withdrawal_details(trans_id, amount, TranscationStatus.APPROVED)
        else:
            DBAccesor.persist_withdrawal_details(trans_id, amount, TranscationStatus.DECLINED)
            self.atm.change_state(CardInjectState(self.atm))


    def dispense_cash(self, trans_id):
        raise IllegalStateException("Invalid state")

    def inject_card(self):
        raise IllegalStateException("Invalid state")

    def get_state_name(self):
        return StateType.WITHDRAWAL_DETAILS_READING_STATE