from typing import Union
from linter.helpers import snake_case_to_pascal_case
from linter.rule import ParamSet, Rule, Severity

# TODO: AUTO-IMPORT RULES
from linter.rules.field_requires_description import FieldRequiresDescription
from linter.rules.view_with_many_fields_requires_fields_hidden_by_default import ViewWithManyFieldsRequiresFieldsHiddenByDefault
from linter.rules.dimension_group_of_type_time_requires_datatype import DimensionGroupOfTypeTimeRequiresDatatype
from linter.rules.dimension_group_of_type_time_requires_timeframe import DimensionGroupOfTypeTimeRequiresTimeframe
from linter.rules.explore_requires_description import ExploreRequiresDescription
from linter.rules.field_sql_html_requires_user_attribute_when_search_terms_found import FieldSqlHtmlRequiresUserAttributeWhenSearchTermsFound


class RuleFactory:
    def __init__(self) -> None:
        pass

    def build(self, rule_name: str, severity: Severity, params: Union[ParamSet, None] = None) -> Rule:
        classname = snake_case_to_pascal_case(rule_name)
        return globals()[classname](severity, params)
