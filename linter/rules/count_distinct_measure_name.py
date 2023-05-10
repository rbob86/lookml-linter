from linter.rule import Rule
from typing import Any, Tuple, Union


class CountDistinctMeasureName(Rule):
    @staticmethod
    def applies_to() -> Tuple[str, ...]:
        return 'measure',

    def run(self, lookml_object, runtime_params: Union[Any, None] = None) -> bool:
        if lookml_object.get('type') == 'count_distinct':
            name = lookml_object.get('name')
            if name:
                return name.startswith('unique_') or name.startswith('count_of_unique_')
        return True

    def message(self) -> str:
        return 'Count Distinct measure name should start with unique_ or count_of_unique_'