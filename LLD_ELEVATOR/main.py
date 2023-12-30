from elevator.elevator import Elevator
from moves_store.uni_direction_move_store import UniDirectionalMoveStore
from state.idle_state import IdleState
from data.floor import Floor
from LLD_ELEVATOR.data.direction import Direction


class Driver:
    def main(self):
        directionStore = UniDirectionalMoveStore()
        elevator = Elevator(directionStore)
        print(directionStore.current_direction)
        elevator.set_current_state(IdleState(elevator))
        elevator.set_current_floor(Floor(0, "Ground"))
        elevator.destine(Floor(4, "Ground"), Direction.UP)
        print(directionStore.current_direction)
        elevator.destine(Floor(5, "Ground"), Direction.UP)
        elevator.destine(Floor(7, "Ground"), Direction.UP)
        print(directionStore.current_direction)
        elevator.set_current_floor(Floor(1, "First"))
        elevator.set_current_floor(Floor(2, "Second"))
        elevator.set_current_floor(Floor(3, "third"))
        elevator.set_current_floor(Floor(4, "fourth"))
        elevator.stop(Floor(4, "fourth"))
        elevator.open(Floor(4, "fourth"))
        elevator.close(Floor(4, "fourth"))
        elevator.set_current_floor(Floor(5, "fifth"))
        elevator.stop(Floor(5, "fourth"))
        elevator.open(Floor(5, "fifth"))
        elevator.close(Floor(5, "fifth"))
        elevator.set_current_floor(Floor(6, "sixth"))
        elevator.set_current_floor(Floor(7, "seventh"))
        print(directionStore.current_direction)
        elevator.stop(Floor(7, "seventh"))
        elevator.open(Floor(7, "seventh"))
        elevator.close(Floor(7, "seventh"))
        print(directionStore.current_direction)
        elevator.destine(Floor(1, "One"), Direction.DOWN)
        print(directionStore.current_direction)


# adding comment

if __name__ == "__main__":
    driver = Driver()
    print("main execution")
    driver.main()
