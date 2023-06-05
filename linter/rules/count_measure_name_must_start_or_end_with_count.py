from linter.rule import Rule
from typing import Any, Tuple, Union


class CountMeasureNameMustStartOrEndWithCount(Rule):
    @staticmethod
    def applies_to() -> Tuple[str, ...]:
        return 'measure',

    def run(self, lookml_object, runtime_params: Union[Any, None] = None) -> bool:
        if lookml_object.get('type') == 'count':
            return lookml_object.get('name').startswith('count_') or lookml_object.get('name').endswith('_count')
        return True