from .split import Split


class PercentSplit(Split):
    def __init__(self, user, percent):
        super().__init__(user)
        self.percent = percent

    def get_percent(self):
        return self.percent

    # expense service will set
    def set_amount(self, amount):
        self.amount = amount
