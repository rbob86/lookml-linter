from linter.rule import Rule
from typing import Any, Tuple
from linter.helpers import is_snake_case


class FieldNameIsSnakeCase(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ("dimension", "measure")

    def run(self, field: Any) -> bool:
        return is_snake_case(field["name"])
