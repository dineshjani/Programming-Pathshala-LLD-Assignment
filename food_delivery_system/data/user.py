from address import Address


class User:
    def __init__(self, user_id, name, phone_number, email_id, address: Address):
        self.user_id = user_id
        self.name = name
        self.phone_number = phone_number
        self.email_id = email_id
        self.address = address
