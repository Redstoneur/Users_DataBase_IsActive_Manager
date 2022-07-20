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
