class IllegalStateException(Exception):
    def __init__(self, message="Illegal State"):
        self.message = message
        super().__init__(self.message)
