from linter.rule import Rule
from typing import Any, Tuple


class AverageMeasureNameMustStartWithAvgOrAverage(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('measure',)

    def run(self, field: Any) -> bool:
        if field.get('type') in ['average', 'average_distinct']:
            return field.get('name').startswith(('avg_', 'average_'))
        return True