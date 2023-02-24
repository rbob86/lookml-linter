from linter.rule import Rule
from typing import Any, Tuple
from re import search


class IncludeShouldNotHaveViewsWithWildcard(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('include',)

    def run(self, include: Any) -> bool:
        pattern = r'\*\.view'
        return not bool(search(pattern, include.get('name')))
