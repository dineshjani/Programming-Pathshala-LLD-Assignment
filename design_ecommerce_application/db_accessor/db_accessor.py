from design_ecommerce_application.data.product import Product
from design_ecommerce_application.data.product_copy import ProductCopy
from typing import List
class DbAccessor:
    def __init__(self):
        pass

    def get_prodcut_by_name(self, product_name) -> List[Product]:
        pass

    def get_product_copy_by_id(self, id) -> ProductCopy:
        pass