from linter.rule import Severity
from linter.rules.average_measure_name_must_start_with_avg_or_average import AverageMeasureNameMustStartWithAvgOrAverage


def test_run_method_successfully_validates_average_measure_name_starts_with_avg_or_average() -> None:
    rule = AverageMeasureNameMustStartWithAvgOrAverage(Severity.ERROR.value)

    field = {'name': 'average_shipping', 'sql': '${order_shipping}', 'type': 'average'}
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_average_measure_name_does_not_start_with_avg_or_average() -> None:
    rule = AverageMeasureNameMustStartWithAvgOrAverage(Severity.ERROR.value)

    field = {'name': 'mean_shipping', 'sql': '${order_shipping}', 'type': 'average'}
    rule_result = rule.run(field)
    assert rule_result == False


def test_run_method_successfully_validates_average_distinct_measure_name_starts_with_avg_or_average() -> None:
    rule = AverageMeasureNameMustStartWithAvgOrAverage(Severity.ERROR.value)

    field = {
        'name': 'avg_shipping',
        'sql': '${order_shipping}',
        'sql_distinct_key': '${order_id}',
        'type': 'average_distinct'
    }
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_average_distinct_measure_name_does_not_start_with_avg_or_average() -> None:
    rule = AverageMeasureNameMustStartWithAvgOrAverage(Severity.ERROR.value)

    field = {
        'name': 'mean_shipping',
        'sql': '${order_shipping}',
        'sql_distinct_key': '${order_id}',
        'type': 'average_distinct'
    }
    rule_result = rule.run(field)
    assert rule_result == False
