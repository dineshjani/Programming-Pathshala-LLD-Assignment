from abc import ABC, abstractmethod


class SqlCommand:
    @abstractmethod
    def execute(self):
        pass
