from design_ecommerce_application.notification.subscriber import Subscriber


class WhatsappBasedSubscriber(Subscriber):
    def __init__(self, whatsapp_number):
        self.whatsapp_number = whatsapp_number

    def notify(self, message: str):
        pass
