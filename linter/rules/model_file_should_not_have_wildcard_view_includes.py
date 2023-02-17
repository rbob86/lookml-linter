from linter.rule import Rule
from typing import Any, Tuple
from re import search


class ModelFileShouldNotHaveWildcardViewIncludes(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('explore',)

    def run(self, explore: Any) -> bool:
        includes = explore.get('includes', [])
        pattern = r'\*.view'
        wildcard_include = [
            bool(search(pattern, include)) for include in includes]
        if any(wildcard_include):
            return False
        return True
