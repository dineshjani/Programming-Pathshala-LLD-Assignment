from product_filter import ProductFilter
from design_ecommerce_application.data.product import Product
from typing import List


class PriceBasedFilter(ProductFilter):
    def __init__(self, price_upper_cap: int, next_filter: ProductFilter):
        self.price_upper_cap = price_upper_cap
        self.next_filter = next_filter

    def filter(self, products: List[Product]) -> List[Product]:
        filtered_products: List[Product] = self.next_filter.filter(products)
        final_products = []
        for product in filtered_products:
            if product.price <= self.price_upper_cap:
                final_products.append(product)
        return final_products
