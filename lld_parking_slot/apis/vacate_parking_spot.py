from lld_parking_slot.vacator.parking_spot_vacator import ParkingSpotVacator


class VacateParkingSpotApi:
    @staticmethod
    def vacate_parking_spot_api(parking_spot):
        return ParkingSpotVacator.vacate_parking_spot(parking_spot)


