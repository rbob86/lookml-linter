from linter.rule import Severity
from linter.rules.view_requires_description import ViewRequiresDescription


def test_run_method_successfully_validates_view_with_description() -> None:
    rule = ViewRequiresDescription(Severity.ERROR.value)

    view = {
        'dimensions': [
            {
                'name': 'id',
                'primary_key': 'yes',
                'sql': '${TABLE}.ID',
                'type': 'number',
            },
            {
                'name': 'inventory_item_id',
                'sql': '${TABLE}.INVENTORY_ITEM_ID',
                'type': 'number',
            },
        ],
        'name': 'order_items',
        'sql_table_name': 'PUBLIC.ORDER_ITEMS',
        'description': 'testing',
    }
    rule_result = rule.run(view)
    assert rule_result == True


def test_run_method_fails_with_view_without_descriptions() -> None:
    rule = ViewRequiresDescription(Severity.ERROR.value)

    view = {
        'dimensions': [
            {
                'name': 'id',
                'primary_key': 'yes',
                'sql': '${TABLE}.ID',
                'type': 'number',
            },
            {
                'name': 'inventory_item_id',
                'sql': '${TABLE}.INVENTORY_ITEM_ID',
                'type': 'number',
            },
        ],
        'name': 'order_items',
        'sql_table_name': 'PUBLIC.ORDER_ITEMS',
    }
    rule_result = rule.run(view)
    assert rule_result == False
