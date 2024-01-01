from design_ecommerce_application.notification.subscriber import Subscriber


class EmailSubscriber(Subscriber):
    def __init__(self, email):
        self.email = email

    def notify(self, message: str):
        pass
