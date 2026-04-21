from typing import Protocol, runtime_checkable


@runtime_checkable
class Database(Protocol):
    def connect(self): ...

    def close(self): ...

    def run_query(self): ...

    def log(self):
        print("Logging DB entity")


class SqlDatabase(Database):
    def connect(self):
        print("Connection to SQL db")

    # def close(self):
    #     print("Closing SQL db connection")

    def run_query(self):
        print("Run SQL db query")

    def sql_db_method(self):
        print("SQL db method")


class NoSqlDatabase(Database):
    def connect(self):
        print("Connection to NoSQL db")

    def close(self):
        print("Closing NoSQL db connection")

    def run_query(self):
        print("Run NoSQL db query")

    def no_sql_db_method(self):
        print("NoSQL db method")


class BorkenDatabase:
    def connect(self):
        print("Connection to SQL db")

    def run_query(self):
        print("Run SQL db query")

    def sql_db_method(self):
        print("SQL db method")


if __name__ == "__main__":
    sql_db = SqlDatabase()
    sql_db.connect()
    no_sq_db = NoSqlDatabase()
    no_sq_db.connect()
    sql_db.log()
    no_sq_db.log()
    print(isinstance(BorkenDatabase(), Database))
