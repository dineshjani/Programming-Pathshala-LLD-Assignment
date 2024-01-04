from sql_command import SqlCommand
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.data.database import Database
from design_inmemory_mysql.constraint.constraint_type import ConstraintType


class RemoveForeignKeyConstraintCommand(SqlCommand):
    def __init__(self, parent_table: Table, child_table: Table):
        self.parent_table = parent_table
        self.child_table = child_table

    def execute(self):
        db: Database = Database.get_instance()
        parent_table: Table = db.get_table(self.parent_table)
        child_table: Table = db.get_table(self.child_table)
        parent_table.remove_constraint(ConstraintType.CHILD_FOREIGN_KEY, child_table)
        child_table.remove_constraint(ConstraintType.PARENT_FOREIGN_KEY, parent_table)
