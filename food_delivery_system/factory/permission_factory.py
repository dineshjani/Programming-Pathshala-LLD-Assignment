from food_delivery_system.Permission.pertmission import Permission
from food_delivery_system.Permission.add_to_cart_permisison import AddToCartPermission
from food_delivery_system.Permission.update_order_permision import UpdateOrderPermission
from food_delivery_system.Permission.delete_cart_permission import DeleteCartPermission


class PermissionFactory:
    @staticmethod
    def get_add_to_cart_permission(user, food_item) -> Permission:
        return AddToCartPermission(user, food_item)

    @staticmethod
    def get_update_order_permision(user, order, status) -> Permission:
        return UpdateOrderPermission(user, order, status)

    @staticmethod
    def get_delete_item_from_cart_permission(user, food_item) -> Permission:
        return DeleteCartPermission(user, food_item)
