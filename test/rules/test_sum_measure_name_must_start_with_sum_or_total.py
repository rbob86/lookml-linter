from linter.rule import Severity
from linter.rules.sum_measure_name_must_start_with_sum_or_total import SumMeasureNameMustStartWithSumOrTotal


def test_run_method_successfully_validates_sum_measure_name_starts_with_sum_or_total() -> None:
    rule = SumMeasureNameMustStartWithSumOrTotal(Severity.ERROR.value)

    field = {'name': 'sum_of_shipping_cost', 'sql': '${order_shipping}', 'type': 'sum'}
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_sum_measure_name_does_not_start_with_sum_or_total() -> None:
    rule = SumMeasureNameMustStartWithSumOrTotal(Severity.ERROR.value)

    field = {'name': 'shipping_total', 'sql': '${order_shipping}', 'type': 'sum'}
    rule_result = rule.run(field)
    assert rule_result == False


def test_run_method_successfully_validates_sum_distinct_measure_name_starts_with_sum_or_total() -> None:
    rule = SumMeasureNameMustStartWithSumOrTotal(Severity.ERROR.value)

    field = {
        'name': 'total_shipping_cost',
        'sql': '${order_shipping}',
        'sql_distinct_key': '${order_id}',
        'type': 'sum_distinct'
    }
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_sum_distinct_measure_name_does_not_start_with_sum_or_total() -> None:
    rule = SumMeasureNameMustStartWithSumOrTotal(Severity.ERROR.value)

    field = {
        'name': 'shipping_cost_sum',
        'sql': '${order_shipping}',
        'sql_distinct_key': '${order_id}',
        'type': 'sum_distinct'
    }
    rule_result = rule.run(field)
    assert rule_result == False
