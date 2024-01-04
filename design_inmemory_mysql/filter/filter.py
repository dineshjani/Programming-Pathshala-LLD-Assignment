from abc import ABC, abstractmethod
from design_inmemory_mysql.data.table import Table


class Filter(ABC):
    @abstractmethod
    def filter(self, table: Table) -> Table:
        pass
