from product_filter import ProductFilter
from design_ecommerce_application.data.product import Product
from typing import List


class IdleFilter(ProductFilter):
    def __init__(self):
        pass

    def filter(self, products:List[Product]) -> List[Product] :
        return products

