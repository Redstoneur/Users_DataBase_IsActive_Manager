from Interface.TableauList import *


def Search(table: Tableau,
           ListInfoSearch: list[tk.Label],
           ListSearch: list[tk.Text]) -> None:
    """
    reload the list of users
    :param table: Table, table of users
    :param ListSearch: list, list of the search
    :param ListInfoSearch: list, list of the info search
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
