from abc import ABC,abstractmethod
from typing import List
from design_ecommerce_application.data.product import Product


class ProductFilter(ABC):

    @abstractmethod
    def filter(self, products:List[Product]) -> List[Product] :
        pass
