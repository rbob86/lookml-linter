from linter.rule import Rule
from typing import Any, Tuple


class ViewRequiresLabel(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('view',)

    def run(self, view: Any) -> bool:
        if not 'label' in view:
            return False
        return True
