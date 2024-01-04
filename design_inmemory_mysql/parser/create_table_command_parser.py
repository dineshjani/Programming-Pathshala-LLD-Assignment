from design_inmemory_mysql.parser.sql_command_parser import SqlCommandParser
from design_inmemory_mysql.command.sql_command import SqlCommand


class CreateTableCommandParser(SqlCommandParser):
    def parse(self, query: str) -> SqlCommand:
        pass


# encapsulation and abstraction
# factory
# parser
# command
# filter
# operator
