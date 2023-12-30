from .elevator_state import ElevatorState
from LLD_ELEVATOR.data.state import State
from LLD_ELEVATOR.data.direction import Direction
from .moving_down_state import MovingDownState
from LLD_ELEVATOR.data.move import Move


class MovingUpState(ElevatorState):
    def __init__(self, elevator):
        self.elevator = elevator

    def destine(self, floor, direction):
        self.elevator.move_store.add_move(Move(floor, direction))
        top_direction = self.elevator.move_store.get_top().destination_direction
        if top_direction == Direction.DOWN:
            self.elevator.set_current_state(MovingDownState(self.elevator))

    def open(self, floor):
        raise RuntimeError("Not an valid action on curren state")

    def close(self, floor):
        raise RuntimeError("Not an valid action on curren state")

    def stop(self, floor):
        from .idle_state import IdleState

        self.elevator.move_store.clear_top()
        self.elevator.set_current_state(IdleState(self.elevator))

    def getName(self):
        return State.MOVINGUP
