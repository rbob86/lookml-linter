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
