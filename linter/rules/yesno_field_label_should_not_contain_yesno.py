from linter.rule import Rule
from typing import Any, Tuple
from re import search, IGNORECASE


class YesnoFieldLabelShouldNotContainYesno(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('dimension', 'measure')

    def run(self, field: Any) -> bool:
        if field.get('type') == 'yesno':
            return not search(r'(yes[_/]no|yesno|yes[_ ]no|yes[_/]No)', field.get('label'), IGNORECASE)
        return True
