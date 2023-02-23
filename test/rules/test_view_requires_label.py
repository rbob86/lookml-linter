from linter.rule import Severity
from linter.rules.view_requires_label import ViewRequiresLabel


def test_run_method_successfully_validates_view_with_label() -> None:
    rule = ViewRequiresLabel(Severity.ERROR.value)

    view = {
        'dimensions': [{'description': 'Was this flight diverted?',
                 'label': 'Is diverted?',
                 'name': 'diverted',
                 'sql': '${TABLE}.diverted',
                 'type': 'yesno'}],
        'label': 'Order Items',
        'measures': [{'description': 'Sum of Cost',
                    'label': 'Sum of Cost',
                    'name': 'sum_of_cost',
                    'sql': '${TABLE}.cost',
                    'type': 'sum_distinct'}],
        'name': 'order_items',
        'sql_table_name': '"PUBLIC"."ORDER_ITEMS"'
    }
    rule_result = rule.run(view)
    assert rule_result == True


def test_run_method_fails_with_view_without_label() -> None:
    rule = ViewRequiresLabel(Severity.ERROR.value)

    view = {
        'dimensions': [{'description': 'Was this flight diverted?',
                 'label': 'Is diverted?',
                 'name': 'diverted',
                 'sql': '${TABLE}.diverted',
                 'type': 'yesno'}],
        'measures': [{'description': 'Sum of Cost',
                    'label': 'Sum of Cost',
                    'name': 'sum_of_cost',
                    'sql': '${TABLE}.cost',
                    'type': 'sum_distinct'}],
        'name': 'order_items',
        'sql_table_name': '"PUBLIC"."ORDER_ITEMS"'
    }
    rule_result = rule.run(view)
    assert rule_result == False