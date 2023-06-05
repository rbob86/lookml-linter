from linter.rule import Severity
from linter.rules.count_measure_name_must_start_or_end_with_count import CountMeasureNameMustStartOrEndWithCount


def test_run_method_successfully_validates_count_measure_name_starts_with_count() -> None:
    rule = CountMeasureNameMustStartOrEndWithCount(Severity.ERROR.value)

    field = {
        'name': 'count_orders',
        'type': 'count'
    }
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_count_measure_name_does_not_start_with_count() -> None:
    rule = CountMeasureNameMustStartOrEndWithCount(Severity.ERROR.value)

    field = {
        'name': 'total',
        'type': 'count'
    }
    rule_result = rule.run(field)
    assert rule_result == False


def test_run_method_successfully_validates_count_distinct_measure_name_starts_with_count() -> None:
    rule = CountMeasureNameMustStartOrEndWithCount(Severity.ERROR.value)

    field = {
        'name': 'count_of_customers',
        'type': 'count_distinct',
        'sql': '${customer_id}'
    }
    rule_result = rule.run(field)
    assert rule_result == True

    field = {
        'name': 'customers_count',
        'type': 'count_distinct',
        'sql': '${customer_id}'
    }
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_successfully_validates_count_distinct_measure_name() -> None:
    rule = CountMeasureNameMustStartOrEndWithCount(Severity.ERROR.value)

    field = {
        'name': 'number_of_customers',
        'type': 'count_distinct',
        'sql': '${customer_id}'
    }
    rule_result = rule.run(field)
    assert rule_result == True
