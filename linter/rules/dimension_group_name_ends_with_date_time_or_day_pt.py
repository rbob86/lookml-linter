from linter.rule import Rule
from typing import Any, Tuple


class DimensionGroupNameEndsWithDateTimeOrDayPt(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('dimension_group',)

    def run(self, dimension_group: Any) -> bool:
        return not dimension_group.get('name').endswith(('_date', '_time', '_day_pt'))