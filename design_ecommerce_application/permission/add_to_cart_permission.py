from design_ecommerce_application.permission.permission import Permission


class AddToCartPermission(Permission):

    def __init__(self, user):
        self.user = user

    def is_permitted(self):
        return False
