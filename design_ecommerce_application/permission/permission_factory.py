from design_ecommerce_application.permission.search_product_permissiom import (
    SearchProductPermission,
)
from design_ecommerce_application.permission.add_to_cart_permission import (
    AddToCartPermission,
)


class PermissionFactory:
    @staticmethod
    def get_search_permission(user):
        # query db .user have permission in db or not
        # construct and return permission
        return SearchProductPermission(user)

    @staticmethod
    def add_to_cart_permission(user):
        return AddToCartPermission(user)
