from linter.rule import Rule
from typing import Any, Tuple, Union


class PrimaryKeyPrefixAndIsHidden(Rule):
    @staticmethod
    def applies_to() -> Tuple[str, ...]:
        return 'dimension',

    def run(self, lookml_object, runtime_params: Union[Any, None] = None) -> bool:
        primary_key = lookml_object.get('primary_key')
        if primary_key:
            return lookml_object.get('name') and lookml_object['name'].startswith('pk_') \
                and lookml_object.get('hidden') and lookml_object['hidden'] == 'yes'
        return True

    def message(self) -> str:
        return 'Primary Key dimension name should start with pk_ and be hidden'