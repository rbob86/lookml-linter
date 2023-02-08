from linter.rule import Rule
from typing import Any, Tuple
from linter.helpers import is_snake_case


class ViewNameIsSnakeCase(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ("view",)

    def run(self, view: Any) -> bool:
        return is_snake_case(view["name"])
