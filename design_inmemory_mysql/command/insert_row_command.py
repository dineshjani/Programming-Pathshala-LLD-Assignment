from sql_command import SqlCommand
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.data.database import Database
from design_inmemory_mysql.data.row import Row
from design_inmemory_mysql.data.key_values_pairs import KeyValPairs
from typing import List


class InsertRowCommand(SqlCommand):
    def __init__(self, table_name: str, key_value_pairs: List[KeyValPairs]):
        self.table_name = table_name
        self.key_val_pairs = key_value_pairs

    def execute(self):
        table:Table = Database.get_instance().get_table(self.table_name)
        row: Row = Row(table.columns)
        for key_val_pairs in self.key_val_pairs:
            row.put(table.get_column(key_val_pairs.key), key_val_pairs.val)


