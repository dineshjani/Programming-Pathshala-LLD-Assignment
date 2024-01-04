from table import Table
from typing import List


class Database:
    instance = None

    def __init__(self, tables):
        self.tables: dict[str, Table] = tables

    @staticmethod
    def get_instance():
        if Database.instance is None:
            Database.instance = Database()
        return Database.instance

    def get_table(self, table_name: str):
        if self.table_name not in self.tables:
            raise RuntimeError("Table Does not exists")
        return self.tables.get(table_name)

    def put_table(self, table_name, table: Table):
        if self.table_name not in self.tables:
            raise RuntimeError("Table Does not exists")
        self.tables[table_name] = table

    def delete_table_name(self, table):
        if table.name not in self.tables:
            raise RuntimeError("Table Does not exists")
        del self.tables[table.name]

    def get_all_tables(self) -> List[Table]:
        return self.tables.keys()
