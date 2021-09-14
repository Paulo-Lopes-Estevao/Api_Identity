from domain.validation.rules.valid import Rule


class Nif():
    def __init__(self):
        self.__validate_nif = Rule()

    def rules(self,value):
        return self.__validate_nif.rules(value)

    def message(self):
        pass