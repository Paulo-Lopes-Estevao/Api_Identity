from .bi import Bi


class Nif():

     __validate_nif = None

     def __init__(self):
         self.__validate_nif = Bi()

     def rules(self,value):
            self.__validate_nif.rules(value)

     def message(self):
         pass