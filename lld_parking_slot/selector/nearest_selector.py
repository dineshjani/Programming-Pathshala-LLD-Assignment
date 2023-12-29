from parking_spot_selector import ParkingSpotSelector


class NearestSpotSelector(ParkingSpotSelector):

    def __init__(self, entry_point):
        self.entry_point = entry_point

    def select_spot(self, spots):
        pass


