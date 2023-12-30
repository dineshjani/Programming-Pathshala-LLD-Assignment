from random_spot_selector import RandomSpotSelector
from nearest_selector import NearestSpotSelector


class SpotSelectionFactory:
    @staticmethod
    def get_nearest_spot_selector(entry_point):
        return NearestSpotSelector(entry_point)

    @staticmethod
    def get_random_spot_selector():
        return RandomSpotSelector()
