from product import Product


class ProductCopy:
    def __init__(self, product:Product, id, is_sold):
        self.product = product
        self.id = id
        self.is_sold = is_sold