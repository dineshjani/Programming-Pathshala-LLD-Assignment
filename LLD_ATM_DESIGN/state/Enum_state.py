from enum import Enum


class StateType(Enum):
    READY = 1
    CARD_READING_STATE = 2
    CARD_INJECT_STATE = 3
    CASH_DISPENSE_STATE = 4
    WITHDRAWAL_DETAILS_READING_STATE = 5
