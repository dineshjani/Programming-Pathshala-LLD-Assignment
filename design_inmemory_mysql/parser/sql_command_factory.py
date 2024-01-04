from create_table_command_parser import CreateTableCommandParser
from sql_command_parser import SqlCommandParser


class SqlCommandFactory:
    parser: SqlCommandParser = None

    def get_parser(self, query: str):
        if "create" in query:
            parser = CreateTableCommandParser()
        # more checks
        return parser
