from abc import ABC,abstractmethod

class ParkingSpotSelector(ABC):

    @abstractmethod
    def select_spot(self, spots):
        pass


