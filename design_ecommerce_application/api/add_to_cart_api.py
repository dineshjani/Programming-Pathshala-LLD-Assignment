from design_ecommerce_application.data.user import User
from design_ecommerce_application.db_accessor.db_accessor import DbAccessor
from design_ecommerce_application.permission.permission_factory import PermissionFactory
from design_ecommerce_application.permission.permission import Permission
class AddToCartApi:
    def __init__(self):
        pass

    def add_to_cart(self, product_id, user: User):
        product_copy = DbAccessor.get_product_copy_by_id(product_id)
        if product_copy is None:
            raise RuntimeError("Invalid Product Id")
        permisison:Permission = PermissionFactory.add_to_cart_permission(user)
        if permisison is None or permisison.is_permitted():\
            raise RuntimeError('Not have a permission')


