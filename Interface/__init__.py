import tkinter as tk
from Interface.DatabaseExecutor import *


########################################################################################################################
############################################### Interface ##############################################################
########################################################################################################################

class Interface(tk.Tk):
    InfoDb: utils.JsonFile
    DB: DatabaseExecutor

    grid_rowconfigure_Max: int = 8
    grid_columnconfigure_Max: int = 3

    def __init__(self, Title: str, Dimension: [int, int], InfoDbPath: str = "./data/infoDB.json"):
        """
        :param InfoDbPath: Path to the infoDB.json file
        """
        super().__init__()
        self.InfoDb = utils.JsonFile(InfoDbPath)
        if self.InfoDb.get("user") is None \
                or self.InfoDb.get("password") is None \
                or self.InfoDb.get("host") is None \
                or self.InfoDb.get("port") is None \
                or self.InfoDb.get("name") is None:
            print("Error: infoDB.json is not correctly formatted")
            print("We don't have all the necessary information to connect to the database")
            print("We don't have : ")
            if self.InfoDb.get("user") is None:
                print("- user")
            if self.InfoDb.get("password") is None:
                print("- password")
            if self.InfoDb.get("host") is None:
                print("- host")
            if self.InfoDb.get("port") is None:
                print("- port")
            if self.InfoDb.get("name") is None:
                print("- name")
            exit()
        else:
            user = self.InfoDb.get("user")
            password = self.InfoDb.get("password")
            host = self.InfoDb.get("host")
            port = self.InfoDb.get("port")
            name = self.InfoDb.get("name")
            self.DB = DatabaseExecutor(user=user, password=password, host=host, port=port, name=name)

        self.title(Title)
        self.geometry(str(Dimension[0]) + "x" + str(Dimension[1]))

        self.grid()
        self.createWidgets()

    def createWidgets(self):
        for i in range(self.grid_rowconfigure_Max):
            self.grid_rowconfigure(i, weight=1)

        for i in range(self.grid_columnconfigure_Max):
            self.grid_columnconfigure(i, weight=1)

        # position
        row: int = 0

        labelTitre = tk.Label(self, text="cc")
        labelTitre.config(font=("Courier", 20))
        labelTitre.grid(row=row, column=0, columnspan=self.grid_columnconfigure_Max, sticky="nsew")

    def quit(self):
        self.master.destroy()
