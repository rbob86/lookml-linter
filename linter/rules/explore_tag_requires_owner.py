from linter.rule import Rule
from typing import Any, Tuple
from re import compile


class ExploreTagRequiresOwner(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('explore',)

    def run(self, explore: Any) -> bool:
        if 'tags' in explore:
            tags = explore['tags']
            for tag in tags:
                pattern = compile(r'^owner:')
                return bool(pattern.match(tag))
