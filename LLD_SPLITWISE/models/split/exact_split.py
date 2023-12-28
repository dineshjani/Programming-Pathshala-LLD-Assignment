from .split import Split
class ExactSplit(Split):
    def __init__(self, user, amount):
        super().__init__(user)
        self.amount = amount


    def get_amount(self):
        return self.amount
    def set_amount(self, amount):
        self.amount = amount