from Interface.UtileFonction import *


########################################################################################################################
############################################### Interface ##############################################################
########################################################################################################################

class Interface(tk.Tk):
    grid_rowconfigure_Max: int = 10
    grid_columnconfigure_Max: int = 4

    def __init__(self, Dimension: [int, int]):
        """
        :param InfoDbPath: Path to the infoDB.json file
        """
        super().__init__()

        self.title(str(Info.get_name()+" - "+Info.get_version()))
        self.geometry(str(Dimension[0]) + "x" + str(Dimension[1]))

        self.grid()
        self.createWidgets()

    def createWidgets(self):

        labelTitre: tk.Label
        labelTitreSubligne: tk.Label

        TableInfoUsers: Tableau

        # labelAddDump: tk.Label
        # textfieldPath: tk.Text
        # RunButton: tk.Button
        # ReloadButton: tk.Button

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

        # TableInfoUsers
        TableInfoUsers = Tableau(self, liste=DB.select(table=str(InfoDb.get("table_users")), select=["*"], limit=10))
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

        print(row)

    def quit(self):
        self.master.destroy()
