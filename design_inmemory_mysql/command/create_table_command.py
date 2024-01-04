from sql_command import SqlCommand
from design_inmemory_mysql.data.column import Column
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.data.database import Database
from typing import Set


class CreateTableCommand(SqlCommand):
    def __init__(self, table_name: str, columns: Set[Column]):
        self.table_name = table_name
        self.columns = columns

    def execute(self):
        table: Table = Table(self.table_name, self.columns)
        Database.get_instance().put_table(self.table_name, table)
        print("Successfully created table")
