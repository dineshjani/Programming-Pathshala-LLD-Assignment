from .card_manager import CardManager


class DebitCardManager(CardManager):
    def validate_card(self, card_details):
        return True

    def validate_withdrawal(self, amount, trans_id):
        pass

    def execute_withdrawal(self, trans_id):
        pass
