from lld_parking_slot.data.entry_point import Entrypoint
from lld_parking_slot.data.spot_selection import SpotSelection
from lld_parking_slot.data.vehicle_type import VehicleType
from lld_parking_slot.manager.vehicle_manager_factory import VehicleManagerFactory
from lld_parking_slot.selector.spot_selection_factory import SpotSelectionFactory
from lld_parking_slot.finder.parking_spot_finder import ParkingSpotFinder


class ParkingSpotApi:
    @staticmethod
    def find_parking_spot(entry_point:Entrypoint, vehicle_type: VehicleType, spot_selection:SpotSelection):
        vehicle_manager = VehicleManagerFactory.get_vehicle_type_manager(vehicle_type)
        if spot_selection == SpotSelection.RANDOM:
             parking_spot_selector = SpotSelectionFactory.get_random_spot_selector()
        elif spot_selection == SpotSelection.NEAREST:
            parking_spot_selector = SpotSelectionFactory.get_nearest_spot_selector(entry_point)
        else:
            raise RuntimeError("invalid spot selection")
        return ParkingSpotFinder(vehicle_manager, parking_spot_selector).find_parking_spot()




