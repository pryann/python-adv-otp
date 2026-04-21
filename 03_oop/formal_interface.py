from abc import ABC, abstractmethod


class Database(ABC):
    # you can use this only, if the Db class are use same parameters
    # def __init__(self, host, port, username, password, db_name):
    #     self.host = host
    #     self.port = port
    #     self.username = username
    #     self.password = password
    #     self.db_name = db_name

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def run_query(self):
        pass

    def log(self):
        print("Logging DB entity")


class SqlDatabase(Database):
    # def __init__(self, host, port, username, password, db_name):
    #     super().__init__(host, port, username, password, db_name)

    def connect(self):
        print("Connection to SQL db")

    def close(self):
        print("Closing SQL db connection")

    def run_query(self):
        print("Run SQL db query")

    def sql_db_method(self):
        print("SQL db method")


class NoSqlDatabase(Database):
    # def __init__(self, host, port, username, password, db_name):
    #     super().__init__(host, port, username, password, db_name)

    def connect(self):
        print("Connection to NoSQL db")

    def close(self):
        print("Closing NoSQL db connection")

    def run_query(self):
        print("Run NoSQL db query")

    def no_sql_db_method(self):
        print("NoSQL db method")


if __name__ == "__main__":
    sql_db = SqlDatabase()
    sql_db.connect()
    no_sq_db = NoSqlDatabase()
    no_sq_db.connect()
    sql_db.log()
    no_sq_db.log()
