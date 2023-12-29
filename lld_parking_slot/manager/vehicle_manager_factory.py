from lld_parking_slot.data.vehicle_type import VehicleType
from two_wheeler_manager import TwoWheelerManager
from four_wheel_manager import FourWheelerManager
from heavy_vehicle_manager import HeavyWheelerManager


class VehicleManagerFactory:
    @staticmethod
    def get_vehicle_type_manager(vehicle_type):
        if vehicle_type == VehicleType.TWO_WHEELER:
            return TwoWheelerManager()
        if vehicle_type == VehicleType.TWO_WHEELER:
            return FourWheelerManager
        if vehicle_type == VehicleType.TWO_WHEELER:
            return HeavyWheelerManager()


