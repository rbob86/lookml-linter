from linter.rule import Rule
from typing import Any, Tuple
from linter.helpers import check_field_naming_convention_by_type


class CountMeasureNameMustStartWithCount(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('measure',)

    def run(self, field: Any) -> bool:
        if field.get('type') in ['count', 'count_distinct']:
            return field.get('name').startswith('count_')
        return True