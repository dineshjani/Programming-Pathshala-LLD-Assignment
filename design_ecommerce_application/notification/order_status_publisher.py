from design_ecommerce_application.notification.publisher import Publisher
from design_ecommerce_application.notification.subscriber import Subscriber
from typing import List


class OrderStatusPublisher(Publisher):
    def __init__(self, subscriber: List[Subscriber]):
        self.subscriber = subscriber

    def add_subscriber(self, subscriber: Subscriber):
        self.subscriber.append(subscriber)

    def remove_subscriber(self, subscriber: Subscriber):
        self.subscriber.remove(subscriber)

    def notify_all(self, message: str):
        for subscriber in self.subscriber:
            subscriber.notify(message)
