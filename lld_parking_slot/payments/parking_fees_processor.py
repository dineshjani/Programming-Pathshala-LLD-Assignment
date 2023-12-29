from lld_parking_slot.data.ticket import Ticket
from lld_parking_slot.manager.vehicle_manager_factory import VehicleManagerFactory
from datetime import datetime


class ParkingFeeProcessor:
    @staticmethod
    def get_parking_fees(ticket: Ticket):
        duration = ticket.vehicle.entry_time - datetime.now()
        return VehicleManagerFactory.get_vehicle_type_manager(ticket.vehicle.vehicle_type).get_parking_fees(duration)

    @staticmethod
    def process_parking_fees(ticket, payment_processor):
        return payment_processor.execute_payment()




