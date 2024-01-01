from abc import ABC, abstractmethod


class Command(ABC):
    """
    merchant and sellers
    For internal module changes we have not to create permission
    """

    def execute(self):
        pass
