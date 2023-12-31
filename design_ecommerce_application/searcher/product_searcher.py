from typing import List
from design_ecommerce_application.data.product import Product
from design_ecommerce_application.db_accessor.db_accessor import DbAccessor
from design_ecommerce_application.filter.filter_factory import FilterFactory
class ProductSearcher:
    def __init__(self):
        pass

    def search_product(self, product_name, filter_details) -> List[Product]:
        # prodcut searcher does not know about filter
        # abstraction applied here
        products:List[Product] = DbAccessor.get_prodcut_by_name(product_name)
        return FilterFactory.get_product_filter(filter_details).filter(products)
