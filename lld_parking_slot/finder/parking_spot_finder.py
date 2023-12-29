class ParkingSpotFinder:
    def __init__(self, vehicle_manager, spot_selector):
        self.vehicle_manager = vehicle_manager
        self.spot_selector = spot_selector

    def find_parking_spot(self):
        select_spot = self.vehicle_manager.get_parking_spots()
        return self.spot_selector.select_spot(select_spot)

