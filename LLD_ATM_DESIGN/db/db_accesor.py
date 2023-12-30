from ..state.Enum_state import StateType


class DBAccesor:
    @staticmethod
    def get_atm_state(machine_id):
        return StateType.READY

    @staticmethod
    def create_new_transcation(self, machine_id):
        return 1

    @staticmethod
    def update_atm_state(self, machine_id, state):
        pass

    @staticmethod
    def persist_card_details(card_details, machine_id):
        pass

    @staticmethod
    def dis_approve_trans(machine_id):
        pass

    @staticmethod
    def cancel_transcation(self, trans_id):
        pass

    @staticmethod
    def persist_withdrawal_details(trans_id, amount, status):
        pass

    @staticmethod
    def mark_as_executed(self, trans_id):
        return 10000
