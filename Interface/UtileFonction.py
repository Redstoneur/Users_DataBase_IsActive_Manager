import tkinter as tk
import platform as plt
from Interface.DatabaseExecutor import *
from Interface.ApplicationInformation import *
from Utilities import *

my_os: str = plt.system()
InfoDb = JsonFile("./data/infoDB.json")
Info = ApplicationInformation("./data/package.json")
DB: DatabaseExecutor

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


def CleanTerminal(errorLabel: tk.Label = None) -> None:
    """
    clean the terminal
    :return: None
    """
    # if the errorLabel is not None
    if errorLabel is not None:
        errorLabel.config(text=" ")

    # if the os is windows
    if my_os == "Windows":
        os.system("cls")
    else:  # if the os is linux
        os.system("clear")


class Tableau(tk.Frame):

    def __init__(self, parent,liste = None, rows=10, columns=10):
        tk.Frame.__init__(self, parent)
        self._widgets = []
        if liste is not None:
            self._rows = len(liste)
            self._columns = len(liste[0])
        else:
            self._rows = rows
            self._columns = columns
        self.create_widgets(liste)

    def create_widgets(self, liste=None):
        for row in range(self._rows):
            current_row = []
            for column in range(self._columns):
                if liste is not None:
                    string: str = str(liste[row][column])
                else:
                    string: str = '(' + str(row) + ':' + str(column) + ')'

                widget = tk.Label(self, text=string)
                widget.grid(row=row, column=column, sticky="nsew")
                current_row.append(widget)
                self._widgets.append(current_row)

    def set(self, row, column, value):
        self._widgets[row][column].config(text=value)

    def get(self, row, column):
        return self._widgets[row][column].cget("text")

    def clear(self):
        self.destroy()


def Reload(table: Tableau) -> None:
    """
    reload the list of users
    :param table: Table, table of users
    :return: None
    """
    table.clear()
    listOfUsers = DB.select(str(InfoDb.get("table_users")), ["*"])
    table.create_widgets(listOfUsers)
