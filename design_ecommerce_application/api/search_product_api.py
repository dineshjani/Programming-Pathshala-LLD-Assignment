from design_ecommerce_application.data.filter_details import FilterDetails
from design_ecommerce_application.searcher.product_searcher import ProductSearcher
from design_ecommerce_application.permission.permission_factory import PermissionFactory
from design_ecommerce_application.data.user import User


class SearchProductApi:
    def __init__(self, product_searcher: ProductSearcher):
        self.product_searcher = product_searcher

    def search(self, product_name, filter_details: FilterDetails, user: User):
        permission = PermissionFactory.get_search_permission(user)
        if permission is None or permission.is_permitted(user):
            raise RuntimeError("Do not have search permission")
        return self.product_searcher.search_product(product_name, filter_details)
