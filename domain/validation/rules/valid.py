from domain.validation.validators.validate import ValidateInterface
import re


class Rule(ValidateInterface):
    
    def rules(self,value):
        pattern = re.compile(r'^\d{9}[A-Z]{2}\d{3}$')
        search_pattern =pattern.search(value)
        return search_pattern.group()

    def message(self):
        return "BI inválido"