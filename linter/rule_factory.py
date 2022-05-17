from typing import Union
from linter.rule import Rule
from linter.rules.field_requires_description import FieldRequiresDescription
from linter.rules.view_with_many_fields_requires_fields_hidden_by_default import ViewWithManyFieldsRequiresFieldsHiddenByDefault
from linter.rules.dimension_group_of_type_time_requires_datatype import DimensionGroupOfTypeTimeRequiresDatatype
from linter.rules.dimension_group_of_type_time_requires_timeframe import DimensionGroupOfTypeTimeRequiresTimeframe
from linter.rules.explore_requires_description import ExploreRequiresDescription
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
