from linter.rule import Rule
from typing import Any, Tuple


class ExploreRequiresAlwaysFilter(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('explore',)

    def run(self, explore: Any) -> bool:
        if not 'always_filter' in explore:
            return False
        return True
