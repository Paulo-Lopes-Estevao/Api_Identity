from domain.validation.rules.valid import Rule

class Bi():
    def __init__(self):
        self.__validate_bi = Rule()

    def rules(self,value):
        return self.__validate_bi.rules(value)
    
    def message(self):
        pass