from models.user import User
from expense_manager import ExpenseManager
from models.split.exact_split import ExactSplit
from models.split.equal_split import EqualSplit
from models.split.percent_split import PercentSplit
from models.expense.enum import ExpenseType


class Driver:
    def main(self):
        expense_manager = ExpenseManager()

        expense_manager.add_user(
            User("u1", "User1", "dinesh.jani@xyz.com", "951155723")
        )
        expense_manager.add_user(
            User("u2", "User2", "dinesh.jani@xyz.com", "951155723")
        )
        expense_manager.add_user(
            User("u3", "User3", "dinesh.jani@xyz.com", "951155721X")
        )
        expense_manager.add_user(
            User("u4", "User4", "dinesh.jani@xyz.com", "951155723")
        )

        while True:
            command = input()
            commands = command.split(" ")
            command_type = commands[0]

            if command_type == "SHOW":
                if len(commands) == 1:
                    expense_manager.show_balances()
                else:
                    expense_manager.show_balance(commands[1])
            elif command_type == "EXPENSE":
                print(commands)
                paid_by = commands[1]
                amount = float(commands[2])
                no_of_users = int(commands[3])
                expense_type = commands[4 + no_of_users]
                splits = []
                i = 0
                while i < no_of_users:
                    user = expense_manager.user_map.get(commands[4 + i])
                    if expense_type == "EQUAL":
                        splits.append(EqualSplit(user))
                    elif expense_type == "EXACT":
                        splits.append(
                            ExactSplit(user, float(commands[5 + no_of_users + i]))
                        )
                    elif expense_type == "PERCENT":
                        splits.append(
                            PercentSplit(user, float(commands[5 + no_of_users + i]))
                        )
                    i += 1

                if expense_type == "EQUAL":
                    expense_manager.add_expense(
                        ExpenseType.EQUAL, amount, paid_by, splits, None
                    )
                elif expense_type == "EXACT":
                    expense_manager.add_expense(
                        ExpenseType.EXACT, amount, paid_by, splits, None
                    )
                elif expense_type == "PERCENT":
                    expense_manager.add_expense(
                        ExpenseType.PERCENT, amount, paid_by, splits, None
                    )


# adding comment

if __name__ == "__main__":
    driver = Driver()
    print("main execution")
    driver.main()
