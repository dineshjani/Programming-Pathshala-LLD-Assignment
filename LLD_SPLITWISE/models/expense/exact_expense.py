from .expense import Expense
from ..split.exact_split import ExactSplit


class ExactExpense(Expense):
    def __init__(self, amount, paid_by, splits, expense_metadata):
        super().__init__(amount, paid_by, splits, expense_metadata)

    def validate(self):
        for split in self.splits:
            if not isinstance(split, ExactSplit):
                return False

        total_amount = self.amount
        sum_split_amount = 0
        for split in self.splits:
            exact_split = split
            sum_split_amount += exact_split.amount
        if total_amount != sum_split_amount:
            return False
        return True
