def snake_case_to_pascal_case(snake_case: str) -> str:
    return snake_case.replace('_', ' ').title().replace(' ', '')
