class Alunos:
    def __init__(self):
        self.__ra = None
        self.__nome = None
        self.__email = None

    @property
    def ra(self):
        return self.__ra

    @ra.setter
    def ra(self, value):
        self.__ra = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value