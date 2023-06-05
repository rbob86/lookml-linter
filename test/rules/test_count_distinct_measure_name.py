from linter.rule import Severity
from linter.rules.count_distinct_measure_name import CountDistinctMeasureName


def test_run_method_successfully_validates_count_measure_name() -> None:
    rule = CountDistinctMeasureName(Severity.ERROR.value)

    field = {
        'name': 'count_of_unique_orders',
        'type': 'count_distinct'
    }
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_count_measure_name() -> None:
    rule = CountDistinctMeasureName(Severity.ERROR.value)

    field = {
        'name': 'total',
        'type': 'count_distinct'
    }
    rule_result = rule.run(field)
    assert rule_result == False


def test_run_method_successfully_validates_count_distinct_measure_name() -> None:
    rule = CountDistinctMeasureName(Severity.ERROR.value)

    field = {
        'name': 'unique_count_of_customers',
        'type': 'count_distinct',
        'sql': '${customer_id}'
    }
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_count_distinct_measure_name() -> None:
    rule = CountDistinctMeasureName(Severity.ERROR.value)

    field = {
        'name': 'number_of_customers',
        'type': 'count_distinct',
        'sql': '${customer_id}'
    }
    rule_result = rule.run(field)
    assert rule_result == False
