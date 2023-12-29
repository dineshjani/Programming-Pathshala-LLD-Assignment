from .elevator_state import ElevatorState
from LLD_ELEVATOR.data.state import State
from LLD_ELEVATOR.data.direction import Direction
from LLD_ELEVATOR.data.move import Move
class MovingDownState(ElevatorState):

    def __init__(self, elevator):
        self.elevator = elevator

    def destine(self, floor, direction):
        from .moving_up_state import MovingUpState
        self.elevator.move_store.add_move((Move(floor, direction)))
        top_direction = self.elevator.move_store.get_top().destination_direction
        if top_direction == Direction.UP:
            self.elevator.set_current_state(MovingUpState(self.elevator))

    def open(self, floor):
        raise RuntimeError("Not an valid action on current state")

    def close(self, floor):
        raise RuntimeError("Not an valid action on current state")

    def stop(self, floor):
        from .idle_state import IdleState
        self.elevator.move_store.clear_top()
        self.elevator.set_current_state(IdleState(self.elevator))

    def getName(self):
        return State.MOVINGDOWN