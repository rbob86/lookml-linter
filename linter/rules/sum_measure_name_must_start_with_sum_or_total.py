from linter.rule import Rule
from typing import Any, Tuple


class SumMeasureNameMustStartWithSumOrTotal(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('measure',)

    def run(self, field: Any) -> bool:
        if field.get('type') in ['sum', 'sum_distinct']:
            return field.get('name').startswith(('sum_', 'total_'))
        return True