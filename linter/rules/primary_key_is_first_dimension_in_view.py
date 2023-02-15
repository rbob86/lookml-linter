from linter.rule import Rule
from typing import Any, Tuple


class PrimaryKeyIsFirstDimensionInView(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('view',)

    def run(self, view: Any) -> bool:
        dimensions = view.get('dimensions', [])
        primary_key_is_first = True
        if len(dimensions) > 0:
            primary_key_is_first = False
            first_dimension = dimensions[0]
            if 'primary_key' in first_dimension:
                primary_key_is_first = True
        return primary_key_is_first