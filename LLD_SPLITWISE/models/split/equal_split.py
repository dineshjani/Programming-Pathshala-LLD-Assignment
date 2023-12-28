from .split import Split
class EqualSplit(Split):
    def __init__(self, user):
        super().__init__(user)

 # expense service will set
    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount