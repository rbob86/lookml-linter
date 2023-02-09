from linter.rule import Rule
from typing import Any, Tuple
from linter.helpers import check_field_naming_convention_by_type


class AverageMeasureNameMustStartWithAvgOrAverage(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('measure',)

    def run(self, field: Any) -> bool:
        field_name = field['name']
        type = field.get('type')
        check_field_type = ['average', 'average_distinct']
        field_name_must_start_with = ['avg','average']

        return check_field_naming_convention_by_type(field_name, type, check_field_type, field_name_must_start_with)
