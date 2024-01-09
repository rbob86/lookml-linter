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
            # Check if all characters are whitespaces
            if all(char.isspace() for char in label):
                return False  # Consider it invalid if all characters are whitespaces

            # Check if the remaining characters follow the rule
            words_in_label = label.split()
            return all(starts_with_capital_or_digit_or_special_char(word) for word in words_in_label)

        return True


    def message(self) -> str:
        return 'Every word in label should start with capital letter, digit, special character or whitespace'
