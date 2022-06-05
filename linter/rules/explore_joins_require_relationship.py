from linter.rule import Rule
from typing import Any, Tuple


class ExploreJoinsRequireRelationship(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('explore',)

    def run(self, explore: Any) -> bool:
        joins = explore.get('joins', [])
        for join in joins:
            if not 'relationship' in join:
                return False
        return True
