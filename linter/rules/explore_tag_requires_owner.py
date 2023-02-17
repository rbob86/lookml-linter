from linter.rule import Rule
from typing import Any, Tuple
from re import compile


class ExploreTagRequiresOwner(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('explore',)

    def run(self, explore: Any) -> bool:
        if not 'tags' in explore:
            return False
        tags = explore.get('tags')
        pattern = compile(r'^owner:')
        tag_contains_owner = [bool(pattern.match(tag)) for tag in tags]
        return any(tag_contains_owner)