from linter.rule import Rule
from typing import Any, Tuple
from linter.helpers import check_field_naming_convention_by_type


class YesnoFieldNameMustStartWithIsOrHas(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('dimension', 'measure')

    def run(self, field: Any) -> bool:
        if field.get('type') in ['yesno']:
            return field.get('name').startswith('is_') or field.get('name').startswith('has_')
        return True
