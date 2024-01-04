from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.filter.filter import Filter


class OrFilter(Filter):
    def __init__(self, filter_1: Filter, filter_2: Filter):
        self.filter_1 = filter_1
        self.filter_2 = filter_2

    def filter(self, table: Table) -> Table:
        table_1: Table = self.filter_1.filter(table)
        table_2: Table = self.filter_2.filter(table)
        rows = set()
        rows.add(table_1.rows)
        rows.add(table_2.rows)
        filtered_table: Table = Table("Temp", table.columns)
        for row in rows:
            filtered_table.add_row(row)
        return filtered_table


# encapsulatiomn order
# command
# filter
# operator
