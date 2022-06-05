from linter.rule import Rule
from typing import Any, Tuple


class ExploreRequiresDescription(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('explore',)

    def run(self, explore: Any) -> bool:
        if not 'description' in explore:
            return False
        return True
