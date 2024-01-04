from abc import ABC, abstractmethod


class SqlCommandParser(ABC):
    @abstractmethod
    def parse(self, query: str):
        pass
