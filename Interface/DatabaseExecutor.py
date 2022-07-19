import mysql.connector as mysql
import Utilities as utils


class DatabaseExecutor:
    name: str
    user: str
    password: str
    host: str
    port: int
    connection = None
    cursor = None

    def __init__(self, user: str, password: str, host: str, port: int, name: str = None):
        self.name: str = name
        self.user: str = user
        self.password: str = password
        self.host: str = host
        self.port: int = port
        self.connection = None
        self.cursor = None


        if self.name is not None:
            self.connectDB()
        else:
            self.connect()

    def connectDB(self):
        try:
            self.connection = mysql.connect(
                database=self.name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
            exit()

    def connect(self):
        try:
            self.connection = mysql.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
            exit()

    def execute(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            print(e)
            exit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def select(self, table: str, select: list[str], where: str = None) -> list:
        query = "SELECT "
        for i in select:
            query += i + ","
        query = query[:-1]
        query += " FROM " + table
        if where is not None:
            query += " WHERE " + where
        self.execute(query)
        return self.fetchall()

    def update(self, table: str, set: list[[str, str]], where: str = None) -> None:
        query = "UPDATE " + table + " SET "
        for i in set:
            query += i[0] + "=" + i[1] + ","
        query = query[:-1]
        if where is not None:
            query += " WHERE " + where
        self.execute(query)