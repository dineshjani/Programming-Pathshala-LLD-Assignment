class Product:
    def __init__(self, id, name, description, price, rating, is_pay_on_delivery, is_available):
        """
        Here some field is optional (like description) we can use builder pattern and make better
        :param id:
        :param name:
        :param description:
        :param price:
        :param rating:
        :param is_pay_on_delivery:
        :param is_available:
        """
        self.id = id  #physical entity
        self.name = name
        self.description = description
        self.price = price
        self.rating = rating
        self.is_pay_on_delivery = is_pay_on_delivery
        self.is_available = is_available
