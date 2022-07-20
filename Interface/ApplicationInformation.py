from Utilities import JsonFile


######################################################################################################################
############################## Class Application Information #########################################################
######################################################################################################################

class ApplicationInformation:
    """
    Class for application information
    """

    __file_path: str
    __file: JsonFile

    name: str
    version: str
    description: str
    author_first_name: str
    author_last_name: str
    email: str

    def __init__(self, file_path: str):
        """
        Constructor
        :param file_path: str, path to the file
        """

        self.__file_path: str = file_path
        self.__file: JsonFile = JsonFile(file_path)

        # noinspection PyTypeChecker
        self.name: str = self.get("name")
        # noinspection PyTypeChecker
        self.version: str = self.get("version")
        # noinspection PyTypeChecker
        self.description: str = self.get("description-en")
        # noinspection PyTypeChecker
        self.author_first_name: str = self.get("author")["firstName"]
        # noinspection PyTypeChecker
        self.author_last_name: str = self.get("author")["lastName"]
        # noinspection PyTypeChecker
        self.email: str = self.get("author")["email"]

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
