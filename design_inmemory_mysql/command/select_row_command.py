from sql_command import SqlCommand
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.filter.filter import Filter
from design_inmemory_mysql.data.database import Database


class SelectRowCommand(SqlCommand):
    def __init__(self, table_name: Table, filter: Filter):
        self.table_name = table_name
        self.filter = filter

    def execute(self):
        table: Table = Database.get_instance().get_table(self.table_name)
        filter_table: Table = self.filter.filter(table)
        for row in filter_table.rows:
            row.print()
