from .card_type import CardType
from .debit_card_manager import DebitCardManager
from .credit_card_manager import CrebitCardManager


class CardManagerFactory:
    @staticmethod
    def get_card_manager(card_type):
        if card_type == CardType.CREDIT:
            return CrebitCardManager()
        if card_type == CardType.DEBIT:
            return DebitCardManager()
        else:
            raise RuntimeError("Invalid card type")
