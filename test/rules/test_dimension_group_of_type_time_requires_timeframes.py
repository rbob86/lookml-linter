from linter.rule import Severity
from linter.rules.dimension_group_of_type_time_requires_timeframes import DimensionGroupOfTypeTimeRequiresTimeframes


def test_run_method_successfully_validates_time_dimension_group_has_timeframes() -> None:
    rule = DimensionGroupOfTypeTimeRequiresTimeframes(Severity.ERROR.value)

    dimension_group = {'type': 'time', 'timeframes': ['date','week','month']}
    rule_result = rule.run(dimension_group)
    assert rule_result == True


def test_run_method_fails_when_time_dimension_group_does_not_have_timeframes() -> None:
    rule = DimensionGroupOfTypeTimeRequiresTimeframes(Severity.ERROR.value)

    dimension_group = {'type': 'time'}
    rule_result = rule.run(dimension_group)
    assert rule_result == False
