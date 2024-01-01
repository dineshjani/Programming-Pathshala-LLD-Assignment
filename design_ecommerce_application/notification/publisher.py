from abc import ABC, abstractmethod
from subscriber import Subscriber


class Publisher(ABC):
    """
    Observer Design pattern
    """

    @abstractmethod
    def add_subscriber(self, subscribe: Subscriber):
        pass

    @abstractmethod
    def remove_subscriber(self, subscribe: Subscriber):
        pass

    @abstractmethod
    def notify_all(self, message: str):
        pass
