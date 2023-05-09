from linter.rule import Rule
from typing import Any, Tuple, Union


class CountMeasureNameMustStartWithCount(Rule):
    def applies_to(self) -> Tuple[str, ...]:
        return 'measure',

    def run(self, lookml_object, runtime_params: Union[Any, None] = None) -> bool:
        if lookml_object.get('type') == 'count':
            return lookml_object.get('name').startswith('count_')
        return True