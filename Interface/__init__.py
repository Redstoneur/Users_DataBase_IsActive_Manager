from Interface.UtileFonction import *


########################################################################################################################
############################################### Interface ##############################################################
########################################################################################################################

class Interface(tk.Tk):
    grid_rowconfigure_Max: int = 5
    grid_columnconfigure_Max: int = 4
    search_column_count: int = len(InfoDb.get("search_column")) * 2

    def __init__(self, Dimension: [int, int]):
        """
        Init the interface
        :param Dimension: [width, height]
        """
        super().__init__()

        self.title(str(Info.get_name() + " - " + Info.get_version()))
        self.geometry(str(Dimension[0]) + "x" + str(Dimension[1]))

        self.grid_columnconfigure_Max = self.search_column_count
        if self.grid_columnconfigure_Max > 4:
            self.grid_columnconfigure_Max = 4

        self.grid_rowconfigure_Max = 5 + self.search_column_count // 4
        if (self.search_column_count / 2) % 2 == 1:
            self.grid_rowconfigure_Max += 1

        self.grid()
        self.createWidgets()

    def createWidgets(self):
        """
        Create the widgets
        :return:
        """

        labelTitre: tk.Label
        labelTitreSubligne: tk.Label

        TableInfoUsers: Tableau

        # labelAddDump: tk.Label
        # textfieldPath: tk.Text
        # RunButton: tk.Button
        ReloadButton: tk.Button

        ListInfoSearchTextField: list[tk.Label]
        ListSearchTextField: list[tk.Text]

        labelAuthor: tk.Label
        labelCopyright: tk.Label
        labelVersion: tk.Label

        for i in range(self.grid_rowconfigure_Max):
            self.grid_rowconfigure(i, weight=1)

        for i in range(self.grid_columnconfigure_Max):
            self.grid_columnconfigure(i, weight=1)

        # position
        row: int = 0

        # label titre
        labelTitre = tk.Label(self, text=Info.get_name())
        labelTitre.config(font=("Courier", 20))
        labelTitre.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1

        # label subtitle
        labelTitreSubligne = tk.Label(self, text=Info.get_version())
        labelTitreSubligne.config(font=("Courier", 10))
        labelTitreSubligne.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1

        ListInfoSearchTextField = []
        ListSearchTextField = []
        for col in range(len(InfoDb.get("search_column")) * 2):
            columnspan: int = 1
            sup: int = 0
            if (self.search_column_count / 2) % 2 == 1 \
                    and (col == self.search_column_count - 2 or col == self.search_column_count - 1):
                sup = 1

            if col % 4 == 0:
                row += 1
            if col % 2 == 1:
                ListSearchTextField.append(tk.Text(self, height=1, width=20))
                ListSearchTextField[-1].grid(row=row, column=col % 4 + sup, columnspan=columnspan, sticky="")
                ListSearchTextField[-1].insert(tk.END, "")
                ListSearchTextField[-1].config(font=("Courier", 10))
            else:
                ListInfoSearchTextField.append(tk.Label(self, text=InfoDb.get("search_column")[col // 2] + " : "))
                ListInfoSearchTextField[-1].grid(row=row, column=col % 4 + sup, columnspan=columnspan, sticky="")
                ListInfoSearchTextField[-1].config(font=("Courier", 10), justify="left", height=1, width=20)

        # position
        row += 1

        ReloadButton = tk.Button(self, text="Search",
                                 command=lambda: Search(table=TableInfoUsers,
                                                        ListInfoSearch=ListInfoSearchTextField,
                                                        ListSearch=ListSearchTextField))
        ReloadButton.config(height=1, width=20)
        ReloadButton.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max, sticky="")

        # position
        row += 1

        # TableInfoUsers
        TableInfoUsers = Tableau(parent=self)
        TableInfoUsers.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max, sticky="nsew")

        # position
        row += 1

        # label Author
        labelAuthor = tk.Label(self, text=Info.get_author())
        labelAuthor.config(font=("Arial", 7))
        labelAuthor.grid(row=row, column=0, sticky="sw")

        # label Copyright
        labelCopyright = tk.Label(self, text=Info.get_email())
        labelCopyright.config(font=("Arial", 7))
        labelCopyright.grid(row=row, column=1, sticky="s")

        # label version
        labelVersion = tk.Label(self, text="v" + Info.get_version())
        labelVersion.config(font=("Arial", 7))
        labelVersion.grid(row=row, column=self.grid_columnconfigure_Max - 1, sticky="se")

    def quit(self):
        """
        Quit the program
        :return:
        """
        self.master.destroy()
