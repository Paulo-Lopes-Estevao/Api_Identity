import abc


class ValidateInterface(abc.ABC):

    def rules(self, value):
        """
        Determine if the validation rule passes.

        - string  value
        - return bool
        """
        pass

    def message(self):
        """
        Get the validation error message.

        - return string
        """
        pass