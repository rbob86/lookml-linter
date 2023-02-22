from linter.rule import Rule
from typing import Any, Tuple
from re import search


class IncludeShouldNotHaveViewsWithWildcard(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('include',)

    def run(self, include: Any) -> bool:
        pattern = r'\*\.view'
        wildcard_include = [bool(search(pattern, i)) for i in include]
        if any(wildcard_include):
            return False
        return True
