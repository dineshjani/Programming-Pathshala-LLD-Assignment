from abc import ABC, abstractmethod


class VehicleTypeManager:
    @abstractmethod
    def get_parking_spots(self):
        pass

    @abstractmethod
    def get_parking_fees(self, duration_in_hours):
        pass
