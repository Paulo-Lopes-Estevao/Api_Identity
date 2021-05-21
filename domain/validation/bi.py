from .rules.valid import Rule

class Bi():

    __validate_bi = None

    def __init__(self):
        self.__validate_bi = Rule()

    def rules(self,value):
        return self.__validate_bi.rules(value)
    
    def message(self):
        pass