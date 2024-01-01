from design_ecommerce_application.notification.subscriber import Subscriber


class SmsBasedSubscriber(Subscriber):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def notify(self, message: str):
        # we can sent message using library
        pass
