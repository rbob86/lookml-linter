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
    pattern = compile(r'^[a-z0-9]+(_[a-z0-9]+)*$')
    return pattern.match(name) is not None

def is_camel_case_with_space(name: str) -> bool:
    pattern = compile(r'^(?:(?:[A-Z]|[^\w\s]|[0-9])[^\s]*\s+)*(?:[A-Z]|[^\w\s]|[0-9])[^\s]*$')
    return pattern.match(name) is not None
