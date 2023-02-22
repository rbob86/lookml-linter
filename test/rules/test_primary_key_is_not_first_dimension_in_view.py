from linter.rule import Severity
from linter.rules.primary_key_is_first_dimension_in_view import PrimaryKeyIsFirstDimensionInView


def test_run_method_successfully_validates_primary_key_is_first_dimension() -> None:
    rule = PrimaryKeyIsFirstDimensionInView(Severity.ERROR.value)

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
    assert rule_result == True


def test_run_method_fails_when_primary_key_is_not_first_dimension() -> None:
    rule = PrimaryKeyIsFirstDimensionInView(Severity.ERROR.value)

    view = {
        'dimensions': [
            {
                'name': 'id',
                'sql': '${TABLE}.ID',
                'type': 'number',
            },
            {
                'name': 'inventory_item_id',
                'primary_key': 'yes',
                'sql': '${TABLE}.INVENTORY_ITEM_ID',
                'type': 'number',
            },
        ],
        'name': 'OrderItems',
        'sql_table_name': 'PUBLIC.ORDER_ITEMS',
    }

    rule_result = rule.run(view)
    assert rule_result == False
