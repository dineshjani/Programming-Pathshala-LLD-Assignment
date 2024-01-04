from sql_command import SqlCommand
from design_inmemory_mysql.data.database import Database
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.constraint.constraint_type import ConstraintType


class DropTableCommand(SqlCommand):
    def __init__(self, table_name: str):
        self.table_name = table_name

    def execute(self):
        db = Database.get_instance()
        table_to_be_deleted: Table = db.get_table(self.table_name)
        if (
            len(
                table_to_be_deleted.get_constraint_by_type(
                    ConstraintType.CHILD_FOREIGN_KEY
                )
            )
            == 0
        ):
            raise RuntimeError(" first delete the child table")
        for table in db.get_table():
            # delete in parent table where point to this table_to_be_related table
            # so parent table will have CHILD_FOREIGN_KEY constraint with this table_to_be_deleted(child table)
            table.remove_constraints(
                ConstraintType.CHILD_FOREIGN_KEY, table_to_be_deleted
            )
        db.delete_table_name(table_to_be_deleted)
        print("Successfully dropped table")
