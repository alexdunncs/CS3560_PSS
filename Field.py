
class Field:
    def __init__(self, name: str, display_name: str, validator=None, validation_pattern_message=None, parser = None):
        self.name = name
        self.display_name = display_name
        self.validator = validator
        self.validation_pattern_message = validation_pattern_message
        self.parser = parser
        self.value = None


    def set(self, value):
        try:
            if self.validator is not None:
                self.validator(value)
            self.value = value if self.parser is None else self.parser(value)
        except ValueError:
            raise ValueError(f'Value {value} does not conform to {self.validation_pattern_message}')

