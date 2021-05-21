from domain.validation.validators.validate import ValidateInterface
import re


class Rule(ValidateInterface):
    
    def rules(self,value):
        pattern = re.compile(r'^\d{9}[A-Z]{2}\d{3}$')
        search_pattern =pattern.search(value)
        try:
            return bool(search_pattern.group())
        except Exception as ex:
            return "False"

    def message(self):
        return "BI inválido"