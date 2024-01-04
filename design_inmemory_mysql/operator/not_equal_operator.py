from design_inmemory_mysql.operator.operator import Operator


class NotEqualToOperator(Operator):
    def operate(self, curr_val: str, expected_val: str):
        return curr_val != expected_val
