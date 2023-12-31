from product_filter import ProductFilter
from design_ecommerce_application.data.product import Product
from typing import List


class RatingBasedFilter(ProductFilter):

    def __init__(self, min_rating:int, next_filter: ProductFilter):
        self.min_rating = min_rating
        self.next_filter = next_filter

    def filter(self, products:List[Product]) -> List[Product] :
        filtered_products: List[Product] = self.next_filter.filter(products)
        final_products = []
        for product in filtered_products:
            if product.rating >= self.min_rating:
                final_products.append(product)
        return final_products
