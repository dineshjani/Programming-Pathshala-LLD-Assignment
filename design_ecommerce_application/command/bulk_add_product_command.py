from command import Command
from design_ecommerce_application.data.user import User
from design_ecommerce_application.data.product_copy import ProductCopy
from typing import List


class BulkAddToProductCommand(Command):
    def __init__(self, user: User, product_copy: List[ProductCopy]):
        self.user = user
        self.product_copy = product_copy

    def execute(self):
        pass
