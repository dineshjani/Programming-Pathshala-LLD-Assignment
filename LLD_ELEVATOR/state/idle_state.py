from .elevator_state import ElevatorState
from LLD_ELEVATOR.data.state import State
from LLD_ELEVATOR.data.direction import Direction
from .moving_up_state import MovingUpState
from .moving_down_state import MovingDownState
from .gate_open_state import GateOpenState
from LLD_ELEVATOR.data.move import Move
class IdleState(ElevatorState):

    def __init__(self, elevator):
        self.elevator = elevator

    def destine(self, floor, direction):
        self.elevator.move_store.add_move(Move(floor, direction))
        top_direction = self.elevator.move_store.get_top().destination_direction
        if top_direction == Direction.UP:
            self.elevator.set_current_state(MovingUpState(self.elevator))
        else:
            self.elevator.set_current_state(MovingDownState(self.elevator))

    def open(self, floor):
        self.elevator.set_current_state(GateOpenState(self.elevator))

    def close(self, floor):
        raise RuntimeError("Not an valid action on current state")

    def stop(self, floor):
        raise RuntimeError("Not an valid action on current state")

    def getName(self):
        return State.IDLE