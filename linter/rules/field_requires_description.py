from linter.rule import Rule
from typing import Any, Tuple


class FieldRequiresDescription(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('dimension', 'measure')

    def run(self, field: Any) -> bool:
        if not 'description' in field:
            return False
        return True
