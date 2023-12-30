from .Enum_state import StateType
from ..custom_exception.exception import IllegalStateException
from ..card.card_manager_factory import CardManagerFactory
from ..db.db_accesor import DBAccesor
from .withdrawl_reading_state import WithdrawlReadingState
from .ready_state import ReadyState


class CardReadingState:
    def __init__(self, atm):
        self.atm = atm

    def init(self):
        raise IllegalStateException("invalid state")

    def cancel_transaction(self, trans_id):
        DBAccesor.cancel_transcation(trans_id)
        self.atm.change_state(ReadyState(self.atm))

    def read_card(self, card_type, card_details):
        result = CardManagerFactory.get_card_manager(card_type).validate_card(
            card_details
        )
        DBAccesor.persist_card_details(card_details, self.atm.machine_id)
        if result:
            self.atm.change_state(WithdrawlReadingState(self.atm))
        else:
            DBAccesor.dis_approve_trans(self.atm.machine_id)
            self.atm.change_state(ReadyState(self.atm))

    def read_withdrawal_details(self, card_type, card_details, trans_id, amount):
        raise IllegalStateException("invalid state")

    def dispense_cash(self, trans_id):
        raise IllegalStateException("invalid state")

    def inject_card(self):
        raise IllegalStateException("invalid state")

    def get_state_name(self):
        return StateType.CARD_READING_STATE
