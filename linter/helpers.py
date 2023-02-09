from typing import List
from re import compile


def snake_case_to_pascal_case(snake_case: str) -> str:
    return snake_case.replace('_', ' ').title().replace(' ', '')


def pascal_case_to_snake_case(pascal_case: str) -> str:
    snake_case = ''
    for char in pascal_case:
        if char.isupper():
            snake_case += '_'
        snake_case += char.lower()
    if snake_case[0] == '_':
        return snake_case[1:]
    return snake_case


def is_snake_case(name: str) -> bool:
    pattern = compile(r'^[a-z][a-z0-9]+(_[a-z0-9]+)*$')
    return pattern.match(name) is not None


def check_field_naming_convention_by_type(
    field_name: str,
    type: str,
    check_field_type: List[str],
    field_must_start_with: List[str]
) -> bool:
    if type not in check_field_type:
        return True
    first_part = field_name.split('_')[0]
    return first_part in field_must_start_with
