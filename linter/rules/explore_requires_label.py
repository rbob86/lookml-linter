from linter.rule import Rule
from typing import Any, Tuple


class ExploreRequiresLabel(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('explore',)

    def run(self, explore: Any) -> bool:
        if not 'label' in explore:
            return False
        return True
