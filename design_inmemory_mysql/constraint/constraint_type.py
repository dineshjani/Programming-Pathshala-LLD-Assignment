from enum import Enum


class ConstraintType(Enum):
    PRIMARY_CONSTRAINTS = 1
    PARENT_FOREIGN_KEY = 2
    CHILD_FOREIGN_KEY = 3
