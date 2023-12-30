from lld_parking_slot.data.vehicle import Vehicle
from lld_parking_slot.data.spot import ParkingSpot
from lld_parking_slot.ticket.ticket_generator import TicketGenerator


class GetTicketApi:
    @staticmethod
    def get_ticket(vehicle: Vehicle, parking_spot: ParkingSpot):
        return TicketGenerator.generate_ticket(vehicle, parking_spot)
