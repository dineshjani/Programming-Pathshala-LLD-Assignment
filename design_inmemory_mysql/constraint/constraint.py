from abc import ABC, abstractmethod
from design_inmemory_mysql.data.row import Row
from design_inmemory_mysql.constraint.constraint_type import ConstraintType


class Constraint(ABC):

    @abstractmethod
    def apply_on_insert_row(self, row_to_be_inserted: Row):
        pass

    @abstractmethod
    def apply_on_update_row(self, row_to_be_updated: Row):
        pass

    @abstractmethod
    def apply_on_delete_row(self, row_to_be_deleted: Row):
        pass

    @abstractmethod
    def get_constraint_type(self) -> ConstraintType:
        pass

    @abstractmethod
    def is_related_constraint(self, related_table):
        pass

    # column change constraint
