from linter.rule import Rule
from typing import Any, Tuple
from linter.helpers import check_field_naming_convention_by_type


class YesnoFieldNameMustStartWithIsOrHas(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('dimension', 'measure')

    def run(self, field: Any) -> bool:
        field_name = field['name']
        type = field.get('type')
        check_field_type = ['yesno']
        field_name_must_start_with = ['is','has']

        return check_field_naming_convention_by_type(field_name, type, check_field_type, field_name_must_start_with)
