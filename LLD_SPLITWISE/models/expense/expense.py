from abc import ABC, abstractmethod


class Expense(ABC):
    def __init__(self, amount, paid_by, splits, metadata):
        self.id = None
        self.amount = amount
        self.paid_by = paid_by
        self.splits = splits
        self.metadata = metadata

    @abstractmethod
    def validate(self):
        pass

    def get_splits(self):
        return self.splits
