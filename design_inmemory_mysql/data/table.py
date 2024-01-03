from typing import Set,List
from row import Row
from column import Column
from design_inmemory_mysql.constraint.constraint import Constraint
from design_inmemory_mysql.constraint.constraint_type import ConstraintType


class Table:
    def __init__(self, name, columns: Set[Column], row: List[Row], constraints: List[Constraint ]):
        self.name = name
        self.columns = columns
        self.rows = row
        self.constraints = constraints

    def add_column(self, col_name: str, col_descriptions: str):
        self.columns.add(col_name)

    def delete_column(self, column_name):
        pass

    def add_row(self, row: Row):
        for constraint in self.constraints:
            constraint.apply_on_insert_row(row)
        self.rows.append(row)

    def delete_row(self, row: Row):
        if row not in self.rows:
            raise RuntimeError("Row does not Exists")

        self.rows.remove(row)

    def add_constraints(self, constraints: Constraint):
        self.constraints.append(constraints)

    def get_constraint_by_type(self, constraint_type: ConstraintType):
        constraints = []
        for constraint in self.constraints:
            if constraint.get_constraint_type() == constraint_type:
                constraints.append(constraint)
        return constraints

    def remove_constraint(self, constraint_type: ConstraintType, related_table):
        list_removable_constraint = []
        for constraint in self.constraints:
            if constraint.get_constraint_type() == constraint_type and constraint.is_related_constraint(related_table):
                list_removable_constraint.append(constraint)

        for constraint in list_removable_constraint:
            self.constraints.remove(constraint)

    def get_column(self, col_name) -> Column:
        for column in self.columns:
            if column.name == col_name:
                return column
