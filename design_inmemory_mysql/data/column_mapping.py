from column import Column


class ColumnMapping:
    def __init__(self, foreign_table_column: Column, current_table_column: Column):
        self.foreign_table_column = foreign_table_column
        self.current_table_column = current_table_column
