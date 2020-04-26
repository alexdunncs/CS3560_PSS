from typing import List

from Field import Field


class CliController:

    @staticmethod
    def populate_field(field: Field):
        while field.value is None:
            try:
                field.set(input(f'Enter value for {field.name}: '))
            except ValueError as err:
                print(err)

    @staticmethod
    def populate_fields(fields: List[Field]):
        for field in fields:
            CliController.populate_field(field)

    @staticmethod
    def fields_as_dict(fields: List[Field]) -> dict:
        result = {}
        for field in fields:
            result.update({field.name: field.value})

        return result
