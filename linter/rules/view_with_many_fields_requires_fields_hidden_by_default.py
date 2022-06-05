from linter.rule import Rule
from typing import Any, Tuple


class ViewWithManyFieldsRequiresFieldsHiddenByDefault(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('view',)

    def run(self, view: Any) -> bool:
        dimensions, measures, dimension_groups = [
            view.get(key, []) for key in ['dimensions', 'measures', 'dimension_groups']]
        number_of_fields = len(dimension_groups) + \
            len(measures) + len(dimensions)
        if number_of_fields >= 50 and not 'fields_hidden_by_default' in view:
            return False
        return True
