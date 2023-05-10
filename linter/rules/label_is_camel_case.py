from linter.helpers import is_camel_case_with_space
from linter.rule import Rule
from typing import Any, Tuple, Union


class LabelIsCamelCase(Rule):
    @staticmethod
    def applies_to() -> Tuple[str, ...]:
        return 'explore', 'view', 'field', 'dimension', 'measure'

    def run(self, lookml_object, runtime_params: Union[Any, None] = None) -> bool:
        return is_camel_case_with_space(lookml_object['label']) if 'label' in lookml_object else True

    def message(self) -> str:
        return 'Label should be in Case Case'