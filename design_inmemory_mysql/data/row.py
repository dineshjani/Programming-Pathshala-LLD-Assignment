from typing import Set, Dict
from column import Column


class Row:
    def __init__(self, columns: Set[Column]):
        self.data: Dict[Column, str] = {}
        for column in columns:
            self.data[column] = None

    def put(self, col, val):
        if col not in self.data:
            raise RuntimeError("Column does not exists in Row")
        self.data[col] = val

    def get(self, col:Column):
        if col not in self.data:
            raise RuntimeError("Column does not exists in Row")
        return self.data[col]

    def print(self): 
        for column in self.data.keys():
            print(f"column_name: ${0} and column_value: ${1}".format(column, self.data[column]))








