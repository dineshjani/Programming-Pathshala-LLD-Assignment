class User:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
