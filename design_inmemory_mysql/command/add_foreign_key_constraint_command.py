from sql_command import SqlCommand
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.data.column_mapping import ColumnMapping
from design_inmemory_mysql.data.database import Database
from design_inmemory_mysql.constraint.child_foreign_key_constraint import (
    ChildForeignKeyConstraint,
)
from design_inmemory_mysql.constraint.parent_foreign_key_constraint import (
    ParentForeignKeyConstraint,
)

from typing import List


class AddForeignKeyConstraintCommand(SqlCommand):
    def __init__(
        self,
        parent_table: Table,
        child_table: Table,
        column_mappings: List[ColumnMapping],
    ):
        self.parent_table = parent_table
        self.child_table = child_table
        self.column_mappings = column_mappings

    def execute(self):
        db: Database = Database.get_instance()
        parent_table: Table = db.get_table(self.parent_table)
        child_table: Table = db.get_table(self.child_table)
        child_column_mapping: ColumnMapping = []
        parent_column_mapping: ColumnMapping = []
        for column_name_mapping in self.column_mappings:
            child_column_mapping.append(
                ColumnMapping(
                    child_table.get_column(column_name_mapping.foreign_table_column),
                    parent_table.get_column(column_name_mapping.current_table_column),
                )
            )
            parent_column_mapping.append(
                parent_table.get_column(column_name_mapping.current_table_column)
            ), ColumnMapping(
                child_table.get_column(column_name_mapping.foreign_table_column)
            )
        parent_table.add_constraints(
            ChildForeignKeyConstraint(child_table, parent_column_mapping)
        )
        child_table.add_constraints(
            ParentForeignKeyConstraint(parent_table, child_column_mapping)
        )
