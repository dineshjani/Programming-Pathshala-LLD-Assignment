from ..split.equal_split import EqualSplit
from .expense import Expense
class EqualExpense(Expense):
    def __init__(self, amount, paid_by, splits, expense_metadata):
        super().__init__(amount, paid_by, splits, expense_metadata)

    def validate(self):
        for split in self.splits:
            if not isinstance(split, EqualSplit):
                return False
        return True
