from linter.rule import Severity
from linter.rules.dimension_group_name_should_not_end_with_date_or_time import DimensionGroupNameShouldNotEndWithDateOrTime


def test_run_method_successfully_validates_dimension_group_does_not_end_with_redundant_word() -> None:
    rule = DimensionGroupNameShouldNotEndWithDateOrTime(Severity.ERROR.value)

    dimension_group = {
        'name': 'delivered',
        'sql': '${TABLE}."DELIVERED_AT"',
        'timeframes': ['raw', 'time', 'date', 'week'],
        'type': 'time'
    }
    rule_result = rule.run(dimension_group)
    assert rule_result == True


def test_run_method_fails_when_dimension_group_ends_with_redundant_word() -> None:
    rule = DimensionGroupNameShouldNotEndWithDateOrTime(Severity.ERROR.value)

    dimension_group = {
        'name': 'arrival_time',
        'sql': '${TABLE}."DELIVERED_AT"',
        'timeframes': ['raw', 'time', 'date', 'week'],
        'type': 'time'
    }
    rule_result = rule.run(dimension_group)
    assert rule_result == False
