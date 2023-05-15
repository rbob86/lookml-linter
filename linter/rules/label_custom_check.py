from linter.helpers import starts_with_capital_or_digit_or_special_char
from linter.rule import Rule
from typing import Any, Tuple, Union


class LabelCustomCheck(Rule):
    @staticmethod
    def applies_to() -> Tuple[str, ...]:
        return 'explore', 'view', 'field', 'dimension', 'measure'

    def run(self, lookml_object, runtime_params: Union[Any, None] = None) -> bool:
        label = lookml_object.get('label')
        if label:
            words_in_label = label.split(' ')
            for word in words_in_label:
                valid = starts_with_capital_or_digit_or_special_char(word)
                if not valid:
                    return False
        return True

    def message(self) -> str:
        return 'Every word in label should start with capital letter, digit or special character'
