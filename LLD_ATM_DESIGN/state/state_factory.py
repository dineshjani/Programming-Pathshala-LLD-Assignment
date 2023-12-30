from .Enum_state import StateType
from .ready_state import ReadyState
from .card_reading_state import CardReadingState
from .card_inject_state import CardInjectState
from .cash_dispening_state import CashDispensingState
from .withdrawl_reading_state import WithdrawlReadingState


class StateFactory:
    @staticmethod
    def get_state(state, atm):
        if state == StateType.READY:
            return ReadyState(atm)
        elif state == StateType.WITHDRAWAL_DETAILS_READING_STATE:
            return WithdrawlReadingState(atm)
        elif state == StateType.CASH_DISPENSE_STATE:
            return CashDispensingState(atm)
        elif state == StateType.CARD_INJECT_STATE:
            return CardInjectState(atm)
        elif state == StateType.CARD_READING_STATE:
            return CardReadingState(atm)
