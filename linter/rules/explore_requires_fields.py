from linter.rule import Rule
from typing import Any, Tuple


class ExploreRequiresFields(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('explore',)

    def run(self, explore: Any) -> bool:
        if not 'fields' in explore:
            return False
        return True
