import tkinter as tk
import platform as plt
from Interface.DatabaseExecutor import *
from Interface.ApplicationInformation import *
from Utilities import *

my_os: str = plt.system()
InfoDb = JsonFile("./data/infoDB.json")
Info = ApplicationInformation("./data/package.json")
DB: DatabaseExecutor

afficher_column: list[str] = list(InfoDb.get("afficher_column"))
afficher_column_table: list[str] = list(InfoDb.get("afficher_column")) + [""]

if InfoDb.get("user") is None \
        or InfoDb.get("password") is None \
        or InfoDb.get("host") is None \
        or InfoDb.get("port") is None \
        or InfoDb.get("name") is None:
    print("Error: infoDB.json is not correctly formatted")
    print("We don't have all the necessary information to connect to the database")
    print("We don't have : ")
    if InfoDb.get("user") is None:
        print("- user")
    if InfoDb.get("password") is None:
        print("- password")
    if InfoDb.get("host") is None:
        print("- host")
    if InfoDb.get("port") is None:
        print("- port")
    if InfoDb.get("name") is None:
        print("- name")
    exit()
else:
    DB = DatabaseExecutor(user=str(InfoDb.get("user")),
                          password=str(InfoDb.get("password")),
                          host=str(InfoDb.get("host")),
                          port=int(str(InfoDb.get("port"))),
                          name=str(InfoDb.get("name"))
                          )


def CleanTerminal() -> None:
    """
    clean the terminal
    :return: None
    """
    # if the os is windows
    if my_os == "Windows":
        os.system("cls")
    else:  # if the os is linux
        os.system("clear")


class Tableau(tk.Frame):
    where: str = "1"
    _columns: int = 10
    _rows: int = 10
    _widgets: list[list[tk.Label]] = []

    def __init__(self, parent):
        """
        constructor of the class
        :param parent: tk.Frame, parent of the widget
        :param liste: list, list of the table
        """
        tk.Frame.__init__(self, parent)

        self.load(clean=False)

    def set(self, row, column, value):
        """
        set the value of the widget
        :param row: int, row of the widget
        :param column: int, column of the widget
        :param value: str, value of the widget
        :return:
        """
        self._widgets[row][column].config(text=value)

    def get(self, row, column):
        """
        get the value of the widget
        :param row: int, row of the widget
        :param column: int, column of the widget
        :return:
        """
        return self._widgets[row][column].cget("text")

    def clear(self) -> None:
        """
        clear the table
        :return:
        """
        for row in self._widgets:
            for widget in row:
                widget.destroy()

    def Columns_AND_Rows(self, liste=None) -> None:
        """
        update the number of columns and rows
        :param liste:
        :return:
        """
        if liste is not None:
            self._rows = len(liste)
            self._columns = len(liste[0])
        else:
            self._rows = 10
            self._columns = 10

    def create_widgets(self, liste=None):
        """
        create the widgets
        :param liste:
        :return:
        """
        for row in range(self._rows):
            current_row = []
            for column in range(self._columns):
                if column == self._columns - 1 and row != 0:
                    actif:bool = DB.select(table=str(InfoDb.get("table_users")),
                                           select=[str(InfoDb.get("column_IsActive"))],
                                           where="id = " + str(liste[row][0])
                    if actif:
                        current_row.append(tk.Label(self, text="Actif", bg="green"))
                    else:
                        current_row.append(tk.Label(self, text="Inactif", bg="red"))
                else:
                    if liste is not None:
                        string: str = str(liste[row][column])
                    else:
                        string: str = '(' + str(row) + ':' + str(column) + ')'
                    widget = tk.Label(self, text=string)

                widget.grid(row=row, column=column, sticky="nsew")
                current_row.append(widget)
                self._widgets.append(current_row)

    def update(self, liste=None, clean: bool = True) -> None:
        """
        update the table
        :param liste:
        :return:
        """
        if clean:
            self.clear()
        self.Columns_AND_Rows(liste=liste)
        self.create_widgets(liste)

    def load(self, clean: bool = True) -> None:
        """
        reload the list of users
        :param table: Table, table of users
        :return: None
        """
        listOfUsers = DB.select(table=str(InfoDb.get("table_users")),
                                select=list(afficher_column),
                                where=self.where,
                                limit=10)
        if listOfUsers is None or len(listOfUsers) == 0:
            self.update(liste=[afficher_column_table], clean=clean)
        else:
            self.update(liste=[afficher_column_table] + listOfUsers, clean=clean)


def Search(table: Tableau,
           ListInfoSearch: list[tk.Label],
           ListSearch: list[tk.Text]) -> None:
    """
    reload the list of users
    :param table: Table, table of users
    :return: None
    """
    # create of Where clause
    where: str = "1"
    for i in range(len(ListInfoSearch)):
        if ListSearch[i].get("1.0", "end-1c") != "":
            where += " AND " + ListInfoSearch[i].cget("text")[:-3] + " LIKE '%" + ListSearch[i].get("1.0",
                                                                                                    "end-1c") + "%'"
    table.where = where
    table.load()

    CleanTerminal()
