class Elevator:
    def __init__(self, move_store):
        self.move_store = move_store

    def get_current_floor(self):
        return self.current_floor

    def set_current_floor(self, floor):
        self.current_floor = floor

    def get_current_state(self):
        return self.get_current_state

    def set_current_state(self, current_state):
        self.current_state = current_state

    def destine(self, floor, direction):
        self.current_state.destine(floor, direction)

    def open(self, floor):
        self.current_state.open(floor)

    def stop(self, floor):
        self.current_state.stop(floor)

    def close(self, floor):
        self.current_state.close(floor)
