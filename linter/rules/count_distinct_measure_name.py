from linter.rule import Rule
from typing import Any, Tuple, Union


class CountDistinctMeasureName(Rule):
    def applies_to(self) -> Tuple[str, ...]:
        return 'measure',

    def run(self, lookml_object, runtime_params: Union[Any, None] = None) -> bool:
        if lookml_object.get('type') == 'count_distinct':
            name = lookml_object.get('name')
            if name:
                return name.startswith('unique_') or name.startswith('count_of_unique_')
        return True