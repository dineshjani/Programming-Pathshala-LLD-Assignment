from abc import ABC, abstractmethod


class ElevatorState(ABC):
    @abstractmethod
    def destine(self, floor, direction):
        pass

    @abstractmethod
    def open(self, floor):
        pass

    @abstractmethod
    def stop(self, floor):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def close(self, floor):
        pass
