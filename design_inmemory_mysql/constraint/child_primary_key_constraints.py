from constraint import Constraint
from design_inmemory_mysql.data.row import Row
from design_inmemory_mysql.data.column import Column
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.constraint.constraint_type import ConstraintType
from typing import Set


class PrimaryKeyConstraint(Constraint):
    def __init__(self, table: Table, primary_keys: Set[Column]):
        self.table = table
        self.primary_keys = primary_keys

    def apply_on_insert_row(self, row_to_be_inserted: Row):
        for row in self.table.rows:
            all_match = True
            for column in self.primary_keys:
                if not row.get(column) == row_to_be_inserted.get(column):
                    all_match = False
                    break
        if all_match:
            raise RuntimeError("Primary key violated")

    def apply_on_update_row(self, row_to_be_updated: Row):
        # need to check constraints
        pass

    def apply_on_delete_row(self, row_to_be_deleted: Row):
        # not action required
        pass

    def get_constraint_type(self) -> ConstraintType:
        return ConstraintType.PRIMARY_CONSTRAINTS

    def is_related_constraint(self, related_table: Table):
        return False
