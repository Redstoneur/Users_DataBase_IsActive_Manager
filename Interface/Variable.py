from Interface.ApplicationInformation import *
from Utilities import *


########################################################################################################################
################################## fonction de chargement des données ##################################################
########################################################################################################################

def verify_set_IsActive_special() -> bool:
    """
    verify if the set_IsActive_special function is correctly defined
    :return:
    """
    set_IsActive_special = InfoDb.get("set_IsActive_special")
    if isinstance(set_IsActive_special, list):
        if len(set_IsActive_special) >= 1:
            for i in set_IsActive_special:
                if isinstance(i, list):
                    if len(i) != 2:
                        return False
                else:
                    return False
        return True
    else:
        return False

def verify_list_colluns(txt:str) -> bool:
    """
    verify if the list_colluns function is correctly defined
    :return:
    """
    list_colluns = InfoDb.get(txt)
    if isinstance(list_colluns, list) and len(list_colluns) >= 1:
        return True
    else:
        return False


def verify_connection():
    """
    verify the connection with the database
    :return:
    """
    if (InfoDb.get("host") == "" or InfoDb.get("host") is None) \
            or (InfoDb.get("port") == "" or InfoDb.get("port") is None) \
            or (InfoDb.get("user") == "" or InfoDb.get("user") is None) \
            or (InfoDb.get("password") == "" or InfoDb.get("password") is None) \
            or (InfoDb.get("name") == "" or InfoDb.get("name") is None) \
            or (InfoDb.get("table_users") == "" or InfoDb.get("table_users") is None) \
            or (InfoDb.get("ID_field") == "" or InfoDb.get("ID_field") is None) \
            or (InfoDb.get("column_IsActive") == "" or InfoDb.get("column_IsActive") is None):

        print("Error: infoDB.json is not correctly formatted")
        print("We don't have all the necessary information to connect to the database")
        print("We don't have : ")

        if InfoDb.get("host") == "" or InfoDb.get("host") is None:
            print(" - host")
        if InfoDb.get("port") == "" or InfoDb.get("port") is None:
            print(" - port")
        if InfoDb.get("user") == "" or InfoDb.get("user") is None:
            print(" - user")
        if InfoDb.get("password") == "" or InfoDb.get("password") is None:
            print(" - password")
        if InfoDb.get("name") == "" or InfoDb.get("name") is None:
            print(" - name")
        if InfoDb.get("table_users") == "" or InfoDb.get("table_users") is None:
            print(" - table_users")
        if InfoDb.get("ID_field") == "" or InfoDb.get("ID_field") is None:
            print(" - ID_field")
        if InfoDb.get("column_IsActive") == "" or InfoDb.get("column_IsActive") is None:
            print(" - column_IsActive")

        exit(1)
    elif not verify_set_IsActive_special():
        print("Error: infoDB.json is not correctly formatted")
        print("We don't have the set_IsActive_special function")
        exit(2)
    elif not verify_list_colluns("search_column"):
        print("Error: infoDB.json is not correctly formatted")
        print("We don't have the search_column function")
        exit(3)
    elif not verify_list_colluns("afficher_column"):
        print("Error: infoDB.json is not correctly formatted")
        print("We don't have the afficher_column function")
        exit(4)
    else:
        DB = DatabaseExecutor(user=str(InfoDb.get("user")),
                              password=str(InfoDb.get("password")),
                              host=str(InfoDb.get("host")),
                              port=int(str(InfoDb.get("port"))),
                              name=str(InfoDb.get("name"))
                              )

        return DB


########################################################################################################################
################################## Variables ###########################################################################
########################################################################################################################

InfoDb: JsonFile = JsonFile("./data/infoDB.json")
Info: ApplicationInformation = ApplicationInformation("./data/package.json")
DB: DatabaseExecutor = verify_connection()

afficher_columns: list[str] = list(InfoDb.get("afficher_column"))
afficher_column_tables: list[str] = list(InfoDb.get("afficher_column")) + ["2002-09-21 02:30:00"]
