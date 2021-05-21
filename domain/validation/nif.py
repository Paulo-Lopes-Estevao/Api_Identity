from .bi import Bi


class Nif():

     __validate_bi = None

     def __init__(self):
         self.__validate_bi = Bi()

     def rules(self,value):
            self.__validate_bi.rules(value)

     def message(self):
         pass