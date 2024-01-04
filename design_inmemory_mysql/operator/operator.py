from abc import ABC, abstractmethod


class Operator(ABC):
    @abstractmethod
    def operate(self, curr_val: str, expected_val: str):
        pass
