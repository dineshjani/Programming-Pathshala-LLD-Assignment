from design_ecommerce_application.permission.permission import Permission
from design_ecommerce_application.db_accessor.db_accessor import DbAccessor

class AddToCartPermission(Permission):
    """

    """
    max_cart_amount = 1000000
    distinct_item_count = 50
    total_item_limit = 1000

    def __init__(self, user):
        self.user = user

    def is_permitted(self):
        """
        extra business reuiremnt to fulfill add-to-cart
        cart_amount
        distinct_item cannot more than 50/something

        Here we write all cart functionlity like product size everthing in cart class which follows abstraction
        :return:
        """
        cart = DbAccessor.get_cart_by_user(self.user)
        if cart.get_cart_amount() > self.max_cart_amount or cart.get_distinct_items_count() > 50 or cart.get_total_item() > self.total_item_limit:
            return False
        return True
