from .elevator_state import ElevatorState
from LLD_ELEVATOR.data.direction import Direction
from .moving_up_state import MovingUpState
from .moving_down_state import MovingDownState
from LLD_ELEVATOR.data.state import State


class GateOpenState(ElevatorState):
    def __init__(self, elevator):
        self.elevator = elevator

    def destine(self, floor, direction):
        raise RuntimeError("Not an valid action on curren state")

    def open(self, floor):
        raise RuntimeError("Not an valid action on curren state")

    def close(self, floor):
        from .idle_state import IdleState

        direction = self.elevator.move_store.get_current_direction()
        if direction == Direction.UP:
            self.elevator.set_current_state(MovingUpState(self.elevator))
        elif direction == Direction.DOWN:
            self.elevator.set_current_state(MovingDownState(self.elevator))
        elif direction == Direction.HALT:
            self.elevator.set_current_state(IdleState(self.elevator))
        else:
            raise RuntimeError("Unsupported direction enum")

    def stop(self, floor):
        raise RuntimeError("Not an valid action on curren state")

    def getName(self):
        return State.GATEOPEN
