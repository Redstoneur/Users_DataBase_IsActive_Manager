from Interface.Variable import *


class Tableau(tk.Frame):
    limit: int = 10
    where: str = "1"
    _columns: int = 10
    _rows: int = 10
    _widgets: list[list[tk.Label]] = []

    def __init__(self, parent, limit: int | None = 10, where: str = "1"):
        """
        constructor of the class
        :param parent: tk.Frame, parent of the widget
        :param liste: list, list of the table
        """
        tk.Frame.__init__(self, parent)

        self.where = where
        self.limit = limit

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
                    relative_ID: int = int(liste[row][0])

                    actif: bool = DB.select(table=str(InfoDb.get("table_users")),
                                            select=[str(InfoDb.get("column_IsActive"))],
                                            where=str(InfoDb.get("ID_field")) + " = " + str(relative_ID)
                                            )[0][0]

                    if actif:
                        current_row.append(tk.Button(self, text="Actif", bg="green",
                                                     command=lambda: self.activity_Button(id=relative_ID,
                                                                                          setActivity=False)))
                    else:
                        current_row.append(tk.Button(self, text="Inactif", bg="red",
                                                     command=lambda: self.activity_Button(id=relative_ID,
                                                                                          setActivity=True)))
                else:
                    if liste is not None:
                        string: str = str(liste[row][column])
                    else:
                        string: str = '(' + str(row) + ':' + str(column) + ')'
                    current_row.append(tk.Label(self, text=string))

                current_row[-1].grid(row=row, column=column, sticky="nsew")
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
                                limit=self.limit)
        if listOfUsers is None or len(listOfUsers) == 0:
            self.update(liste=[afficher_column_table], clean=clean)
        else:
            self.update(liste=[afficher_column_table] + listOfUsers, clean=clean)

    def activity_Button(self, id: int, setActivity: bool) -> None:
        """
        the effect of the activity button
        :return:
        """
        DB.update(table=str(InfoDb.get("table_users")),
                  set=[[str(InfoDb.get("column_IsActive")), str(setActivity)]] +
                      list(InfoDb.get("set_IsActive_special")),
                  where=str(InfoDb.get("ID_field")) + " = " + str(id))

        self.load()
