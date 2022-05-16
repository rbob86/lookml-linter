from typing import Union
from linter.rule import Rule
from linter.rules.field_should_have_description import FieldShouldHaveDescription
from linter.rules.view_hidden_by_default_enabled import ViewHiddenByDefault
from linter.rules.dimension_group_datatype_definition import DimensionGroupDataTypeDefinition
from linter.rules.dimension_group_timeframe_definition import DimensionGroupTimeframeDefinition
from linter.rules.explore_description_definition import ExploreDescriptionDefinition
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
