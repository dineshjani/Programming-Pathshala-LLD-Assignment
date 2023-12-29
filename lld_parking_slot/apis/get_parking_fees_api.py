from lld_parking_slot.payments.parking_fees_processor import ParkingFeeProcessor
from lld_parking_slot.payments.payment_mode import PaymentMode
from lld_parking_slot.payments.payment_processor_factory import PaymentProcessorFactory

class GetParkingFeesApi:

    @staticmethod
    def get_parking_fees_api(ticket):
        return ParkingFeeProcessor.get_parking_fees(ticket)

    @staticmethod
    def pay_parking_fees_api(ticket, payment_mode, payment_details:dict):
        payment_processor = None
        if payment_mode == PaymentMode.CARD:
            payment_processor = PaymentProcessorFactory.get_card_payment_processor(payment_details.get('amount'),payment_details.get('card_details') )
        elif payment_mode == PaymentMode.CASH:
            payment_processor = PaymentProcessorFactory.get_cash_payment_processor(payment_details.get('amount'))
        else:
            raise RuntimeError("Invalid or un-supported payment_mode")
        return ParkingFeeProcessor.process_parking_fees(ticket, payment_processor)










