from LLD_ELEVATOR.data.direction import Direction
from .moves_store import MoveStore
import heapq


class UniDirectionalMoveStore(MoveStore):
    def __init__(self):
        self.upwards_moves = []  # min-heap
        self.downward_moves = []  # max-heap
        self.current_direction = Direction.HALT

    def add_move(self, move):
        if len(self.upwards_moves) == 0 and len(self.downward_moves) == 0:
            self.current_direction = move.destination_direction
        a = type(move.destination_direction)
        b = type(Direction.UP)
        if move.destination_direction == Direction.UP:
            heapq.heappush(self.upwards_moves, (move.destination_floor.number, move))
        else:
            heapq.heappush(
                self.downward_moves, (-1 * move.destination_floor.number, move)
            )

    def get_top(self):
        if len(self.downward_moves) == 0 and len(self.upwards_moves) == 0:
            return None
        if self.current_direction == Direction.UP:
            return None if len(self.upwards_moves) == 0 else self.upwards_moves[0][1]
        else:
            return None if len(self.downward_moves) == 0 else self.downward_moves[0][1]

    def clear_top(self):
        if len(self.downward_moves) == 0 and len(self.upwards_moves) == 0:
            raise RuntimeError("Illegal operation on empty list")
        if self.current_direction == Direction.UP:
            heapq.heappop(self.upwards_moves)
            if len(self.upwards_moves) == 0:
                if len(self.downward_moves) != 0:
                    self.current_direction = Direction.DOWN
                else:
                    self.current_direction = Direction.HALT
        else:
            heapq.heappop(self.downward_moves)
            if len(self.downward_moves) == 0:
                if len(self.upwards_moves) != 0:
                    self.current_direction = Direction.UP
                else:
                    self.current_direction = Direction.HALT

    def get_current_direction(self):
        return self.current_direction
