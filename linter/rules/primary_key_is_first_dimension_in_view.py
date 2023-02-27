from linter.rule import Rule
from typing import Any, Tuple


class PrimaryKeyIsFirstDimensionInView(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('view',)

    def run(self, view: Any) -> bool:
        dimensions = view.get('dimensions', [])
        if len(dimensions) > 0 and dimensions[0].get('primary_key') != 'yes':
            return False
        return True
