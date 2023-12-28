from models.expense.enum import ExpenseType
from models.expense.exact_expense import ExactExpense
from models.expense.percent_expense import PercentExpense
from models.expense.equal_expense import EqualExpense

class ExpenseService:
    @staticmethod
    def create_expense(expense_type, amount, paid_by, splits, expense_metadata):
        if expense_type == ExpenseType.EXACT:
            return ExactExpense(amount, paid_by, splits, expense_metadata)
        elif expense_type == ExpenseType.PERCENT:
            for split in splits:
                percent_split = split
                split.set_amount((amount * percent_split.get_percent()) / 100.0)
            return PercentExpense(amount, paid_by, splits, expense_metadata)
        elif expense_type == ExpenseType.EQUAL:
            total_splits = len(splits)
            split_amount = round(amount * 100 / total_splits) / 100.0
            for split in splits:
                split.set_amount(split_amount)
            return EqualExpense(amount, paid_by, splits, expense_metadata)
        else:
            return None
