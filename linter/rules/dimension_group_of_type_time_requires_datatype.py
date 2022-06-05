from linter.rule import Rule
from typing import Any, Tuple


class DimensionGroupOfTypeTimeRequiresDatatype(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('dimension_group',)

    def run(self, dimension_group: Any) -> bool:
        type = dimension_group.get('type')
        if type == 'time' and not 'datatype' in dimension_group:
            return False
        return True
