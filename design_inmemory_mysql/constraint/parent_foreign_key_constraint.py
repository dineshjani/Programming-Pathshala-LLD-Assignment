from constraint import Constraint
from design_inmemory_mysql.data.row import Row
from design_inmemory_mysql.data.column import Column
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.data.column_mapping import ColumnMapping
from design_inmemory_mysql.constraint.constraint_type import ConstraintType
from typing import List


class ParentForeignKeyConstraint(Constraint):
    def __init__(self, parent_table: Table, column_mapping: List[ColumnMapping]):
        self.parent_table = parent_table
        self.column_mapping = column_mapping

    def apply_on_insert_row(self, row_to_be_inserted: Row):
        for row in self.parent_table.rows:
            all_match = True
            for column_mapping in self.column_mapping:
                if row.get(
                    column_mapping.foreign_table_column
                ) != row_to_be_inserted.get(column_mapping.current_table_column):
                    all_match = False
            if all_match:
                return
        raise RuntimeError("Parent Foreign key constraints violated")

    def apply_on_update_row(self, row_to_be_updated: Row):
        # need to check constraints
        pass

    def apply_on_delete_row(self, row_to_be_deleted: Row):
        # not action required
        pass

    def get_constraint_type(self) -> ConstraintType:
        return ConstraintType.PARENT_FOREIGN_KEY

    def is_related_constraint(self, related_table: Table):
        return self.parent_table.name == related_table.name
