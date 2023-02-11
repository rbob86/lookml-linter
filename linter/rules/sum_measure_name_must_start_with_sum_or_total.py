from linter.rule import Rule
from typing import Any, Tuple
from linter.helpers import check_field_naming_convention_by_type


class SumMeasureNameMustStartWithSumOrTotal(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('measure',)

    def run(self, field: Any) -> bool:
        if field.get('type') in ['sum', 'sum_distinct']:
            return field.get('name').startswith('sum_') or field.get('name').startswith('total_')
        return True