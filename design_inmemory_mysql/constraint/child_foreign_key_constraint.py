from constraint import Constraint
from design_inmemory_mysql.data.row import Row
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.data.column_mapping import ColumnMapping
from design_inmemory_mysql.constraint.constraint_type import ConstraintType
from typing import List


class ChildForeignKeyConstraint(Constraint):
    def __init__(self, child_table: Table, column_mapping:  List[ColumnMapping]):
        self.child_table = child_table
        self.column_mapping = column_mapping

    def apply_on_insert_row(self, row_to_be_inserted: Row):
        pass
        # not action required

    def apply_on_update_row(self, row_to_be_updated: Row):
        # need to check constraints
        pass

    def apply_on_delete_row(self, row_to_be_deleted: Row):
        for row in self.child_table.rows:
            all_match = True
            for column_mapping in self.column_mapping:
                if row.get(column_mapping.foreign_table_column) != row_to_be_deleted.get(column_mapping.current_table_column):
                    all_match = False
            if all_match:
                raise RuntimeError("Child Foreign key constraint violated")

    def get_constraint_type(self) -> ConstraintType:
        return ConstraintType.CHILD_FOREIGN_KEY

    def is_related_constraint(self, related_table: Table):
        return self.child_table.name == related_table.name
