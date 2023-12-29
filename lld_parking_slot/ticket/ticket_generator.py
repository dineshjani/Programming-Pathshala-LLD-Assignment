from lld_parking_slot.data.ticket import Ticket
class TicketGenerator:
    @staticmethod
    def generate_ticket(vehicle, parking_spot):
        ticket_numer = TicketGenerator.get_unique_ticket_num
        # logic to check is spot is free or not and also here need to handle race condition
        return Ticket(ticket_numer, vehicle, parking_spot)

    @staticmethod
    def get_unique_ticket_num():
        return ""


