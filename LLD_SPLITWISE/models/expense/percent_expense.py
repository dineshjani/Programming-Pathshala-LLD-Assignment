from .expense import Expense
from ..split.percent_split import PercentSplit

class PercentExpense(Expense):
    def __init__(self, amount, paid_by, splits, expense_metadata):
        super().__init__(amount, paid_by, splits, expense_metadata)

    def validate(self):
        for split in self.splits:
            if not isinstance(split, PercentSplit):
                return False

        total_percent = 100
        sum_split_percent = 0
        for split in self.splits:
            percent_split = split
            sum_split_percent += percent_split.percent
        if total_percent != sum_split_percent:
            return False

        return True