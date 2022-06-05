from linter.rule import Rule
from typing import Any, Tuple


class ExploreJoinsContainManyToManyRelationship(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('explore',)

    def run(self, explore: Any) -> bool:
        joins = explore.get('joins', [])
        for join in joins:
            if 'relationship' in join:
                if join['relationship'] == 'many_to_many':
                    return False
        return True
