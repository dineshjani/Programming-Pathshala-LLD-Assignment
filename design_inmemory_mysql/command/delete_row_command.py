from sql_command import SqlCommand
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.data.database import Database
from design_inmemory_mysql.data.row import Row
from design_inmemory_mysql.filter.filter import Filter


class DeleteRowCommand(SqlCommand):
    def __init__(self, table_name: str, _filter: Filter):
        self.table_name = table_name
        self.filter = _filter

    def execute(self):
        table: Table = Database.get_table(self.table_name)
        filter_table: Table = self.filter.filter(self.table_name)
        for row in filter_table.rows:
            table.delete_row(row)
