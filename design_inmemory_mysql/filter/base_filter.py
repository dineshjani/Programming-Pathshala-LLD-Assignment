from abc import ABC, abstractmethod
from design_inmemory_mysql.data.table import Table
from design_inmemory_mysql.filter.filter import Filter


class BaseFilter(Filter):
    def __init__(self, column, operator, expected_val):
        self.column = column
        self.operator = operator
        self.expected_val = expected_val

    def filter(self, table: Table) -> Table:
        filter_table: Table = Table("Temp", table.columns)
        for row in table.rows:
            if self.operator.operate(row.get(self.column), self.expected_val):
                filter_table.add_row(row)
        return filter_table


# encapsulatiomn order
# command
# filter
# operator
