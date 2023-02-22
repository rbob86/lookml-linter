from linter.rule import Rule
from typing import Any, Tuple


class PrimaryKeyIsFirstDimensionInView(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('view',)

    def run(self, view: Any) -> bool:
        dimensions = view.get('dimensions', [])
        if len(dimensions) > 0 and 'primary_key' not in dimensions[0]:
            return False
        return True
