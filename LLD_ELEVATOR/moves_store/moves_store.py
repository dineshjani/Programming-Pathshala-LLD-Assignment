from abc import ABC, abstractmethod

# from ..data.move import Move
class MoveStore(ABC):
    @abstractmethod
    def add_move(self, move):
        pass

    @abstractmethod
    def get_top(self):
        pass

    @abstractmethod
    def clear_top(self):
        pass

    @abstractmethod
    def get_current_direction(self):
        pass
