from typing import Union
from linter.rule import Rule
from linter.rules.field_should_have_description import FieldShouldHaveDescription
from linter.rules.view_should_have_z import ViewShouldHaveZ
from linter.severity import Severity


class RuleFactory:
    def __init__(self) -> None:
        pass

    def build(self, rule_name: str, severity: Union[Severity, None] = None) -> Rule:
        classname = self.__rule_name_to_classname(rule_name)
        rule_class = globals()[classname]
        if severity is None:
            severity = rule_class.default_severity()
        return globals()[classname](severity)

    def __rule_name_to_classname(self, rule_name: str) -> str:
        return rule_name.replace('_', ' ').title().replace(' ', '')
