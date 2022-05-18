from linter.rules.dimension_group_of_type_time_requires_timeframe import DimensionGroupOfTypeTimeRequiresTimeframe


def test_run_method_successfully_validates_time_dimension_group_has_timeframe() -> None:
    rule = DimensionGroupOfTypeTimeRequiresTimeframe()

    dimension_group = {'type': 'time', 'timeframe': ['day']}
    rule_result = rule.run(dimension_group)
    assert rule_result == True


def test_run_method_fails_when_time_dimension_group_does_not_have_timeframe() -> None:
    rule = DimensionGroupOfTypeTimeRequiresTimeframe()

    dimension_group = {'type': 'time'}
    rule_result = rule.run(dimension_group)
    assert rule_result == False
