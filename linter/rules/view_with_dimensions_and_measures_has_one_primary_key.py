from linter.rule import Rule
from typing import Any, Tuple


class ViewWithDimensionsAndMeasuresHasOnePrimaryKey(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('view',)

    def run(self, view: Any) -> bool:
        dimensions, measures = [
            view.get(key, []) for key in ['dimensions', 'measures']]
        has_primary_key = True
        if len(measures) > 0 and len(dimensions) > 0:
            has_primary_key = False
            for dimension in dimensions:
                if 'primary_key' in dimension:
                    if has_primary_key:
                        return False
                    has_primary_key = True
        return has_primary_key
