from design_ecommerce_application.data.product_copy import ProductCopy
from typing import List


class Cart:
    def __init__(self, id, products: List[ProductCopy]):
        self.id = id
        self.products = products

    def add(self, product_copy: ProductCopy):
        self.products.append(product_copy)

    def remove(self, product_copy: ProductCopy):
        if product_copy not in self.products:
            raise RuntimeError("Product does not exist")
        self.products.remove(product_copy)

    def get_cart_amount(self):
        amount = 0
        for product in self.products:
            amount = amount + product.product.price
        return amount

    def get_distinct_items_count(self):
        distinct_ids = set()
        for product_copy in self.products:
            distinct_ids.add(product_copy.product.id)
        return len(distinct_ids)

    def get_total_item(self):
        return len(self.products)
