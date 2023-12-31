from product_filter import ProductFilter
from design_ecommerce_application.data.product import Product
from typing import List


class PayOnDelFilter(ProductFilter):
    def __init__(self, is_pay_on_delivery: bool, next_filter: ProductFilter):
        self.is_pay_on_delivery = is_pay_on_delivery
        self.next_filter = next_filter

    def filter(self, products: List[Product]) -> List[Product]:
        filtered_products: List[Product] = self.next_filter.filter(products)
        final_products = []
        for product in filtered_products:
            if product.is_pay_on_delivery == self.is_pay_on_delivery:
                final_products.append(product)
        return final_products
