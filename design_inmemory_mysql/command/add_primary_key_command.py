from sql_command import SqlCommand
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.constraint.constraint_type import ConstraintType
from typing import List
from design_inmemory_mysql.constraint.child_primary_key_constraints import PrimaryKeyConstraint


class AddPrimaryKeyConstraintCommand(SqlCommand):
    def __init__(self, table_name: str, column_names: List[str]):
        self.table_name = table_name
        self.column_names = column_names

    def execute(self):
        table: Table = Table(self.table_name, self.columns)
        columns = set()
        for col in self.column_names:
            columns.add(table.get_column(col))
        constraints = table.get_constraint_by_type(ConstraintType.PRIMARY_CONSTRAINTS)
        if len(constraints) != 0:
            raise RuntimeError("Primary key constraints exists")
        table.add_constraints(PrimaryKeyConstraint(table, columns))



