from ..db.db_accesor import DBAccesor
from ..state.state_factory import StateFactory


class Atm:
    def __init__(self, machine_id):
        self.machine_id = machine_id
        # should not depend on concrete class
        self.state = StateFactory.get_state(DBAccesor.get_atm_state(machine_id), self)

    def init(self):
        return self.state.init()

    def cancel(self, trans_id):
        self.state.cancel(trans_id)

    def read_card(self, card_type, card_num, pin, name):
        return self.state.read_card(card_type, card_num, pin, name)

    def read_withdrawl_deatils(self, card_type, card_num, pin, name):
        return self.state.read_withdrawl_deatils(card_type, card_num, pin, name)

    def dispense_cash(self, trans_id):
        return self.state.dispense_cash(trans_id)

    def inject_card(self):
        return self.state.inject_card()

    def change_state(self, state):
        self.state = state
        DBAccesor.update_atm_state(self.machine_id, state.get_state_name())

    # we can writes setter for machine_id and state
