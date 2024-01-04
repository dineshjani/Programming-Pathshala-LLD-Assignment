from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.filter.filter import Filter
from typing import Set


class AndFilter(Filter):
    def __init__(self, filter_1: Filter, filter_2: Filter):
        self.filter_1 = filter_1
        self.filter_2 = filter_2

    def filter(self, table: Table) -> Table:
        table_1: Table = self.filter_1.filter(table)
        table_2: Table = self.filter_2.filter(table_1)
        return table_2


# encapsulatiomn order
# command
# filter
# operator
