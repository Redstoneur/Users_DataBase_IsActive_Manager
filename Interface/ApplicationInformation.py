from Utilities import JsonFile, Error


######################################################################################################################
############################## Class Application Information #########################################################
######################################################################################################################

class ApplicationInformation:
    """
    Class for application information
    """

    listName_en = ["name", "version", "description-en", ["author", "firstName", "lastName", "email"]]
    listName_fr = ["name", "version", "description-fr", ["author", "firstName", "lastName", "email"]]

    __file_path: str
    __file: JsonFile

    name: str
    version: str
    description: str
    author_first_name: str
    author_last_name: str
    email: str

    def __init__(self, file_path: str, language: str = "en"):
        """
        Constructor
        :param file_path: str, path to the file
        """
        listName: list = []

        self.__file_path: str = file_path
        self.__file: JsonFile = JsonFile(file_path)

        if language == "en":
            listName: list = self.listName_en
        elif language == "fr":
            listName: list = self.listName_fr
        else:
            exit(Error(success=False, message="Language not supported", code=500))

        for i in range(len(listName)):
            elemment: object = listName[i]
            if type(elemment) is list:
                e: str = elemment[0]
            else:
                e: str = str(elemment)

            var: object = self.get(e)

            if var is None:
                exit(Error(success=False, message="The " + e + " is not defined", code=404).__str__())
            elif isinstance(var, str):
                if e == "name":
                    self.name: str = var
                elif e == "version":
                    self.version: str = var
                elif e == "description-en":
                    self.description: str = var
                elif e == "description-fr":
                    self.description: str = var
                else:
                    exit(Error(success=False, message="The " + e + " is not correctly defined", code=500).__str__())
            elif isinstance(var, dict):
                if e == "author":
                    self.author_first_name: str = var[elemment[1]]
                    self.author_last_name: str = var[elemment[2]]
                    self.email: str = var[elemment[3]]
                else:
                    exit(Error(success=False, message="The " + e + " is not correctly defined", code=500).__str__())
            else:
                print(Error(success=False, message="The " + e +" is not defined", code=404).__str__())

    def get(self, key: str) -> object:
        """
        get value from the file
        :param key: str, key of the value
        :return: str, value
        """

        return self.__file.get(key)

    def haveData(self) -> bool:
        """
        check if the file have data
        :return: bool, True if the file have data, False if not
        """

        # if have information
        if self.name is not None \
                and self.version is not None \
                and self.description is not None \
                and self.author_first_name is not None \
                and self.author_last_name is not None:
            return True
        else:
            return False

    def __str__(self) -> str:
        """
        print information about the program
        :return: str, information about the program
        """
        return "Name: " + self.name + "\n" + \
               "Version: " + self.version + "\n" + \
               "Description: " + self.description + "\n" + \
               "Author: " + self.author_first_name + " " + self.author_last_name + "\n"

    def get_name(self) -> str:
        """
        get name of the program
        :return: str, name of the program
        """

        return self.name

    def get_version(self) -> str:
        """
        get version of the program
        :return: str, version of the program
        """

        return self.version

    def get_description(self) -> str:
        """
        get description of the program
        :return: str, description of the program
        """

        return self.description

    def get_author_first_name(self) -> str:
        """
        get first name of the author
        :return: str, first name of the author
        """

        return self.author_first_name

    def get_author_last_name(self) -> str:
        """
        get last name of the author
        :return: str, last name of the author
        """

        return self.author_last_name

    def get_author(self) -> str:
        """
        get author of the program
        :return: str, author of the program
        """

        return self.author_first_name + " " + self.author_last_name

    def get_email(self) -> str:
        """
        get email of the author
        :return: str, email of the author
        """

        return self.email
