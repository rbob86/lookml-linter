from linter.rule import Severity
from linter.rules.view_description_requires_minimum_length import ViewDescriptionRequiresMinimumLength


def test_run_method_successfully_validates_view_with_minimum_length_description() -> (
    None
):
    params = {"min_length": 20}
    rule = ViewDescriptionRequiresMinimumLength(Severity.ERROR.value, params)

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
        'description': 'long description with more than 20 characters',
    }
    rule_result = rule.run(view)
    assert rule_result == True


def test_run_method_successfully_validates_view_without_description() -> None:
    params = {"min_length": 20}
    rule = ViewDescriptionRequiresMinimumLength(Severity.ERROR.value, params)

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


def test_run_method_fails_with_view_with_short_description() -> None:
    params = {"min_length": 20}
    rule = ViewDescriptionRequiresMinimumLength(Severity.ERROR.value, params)

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
        'description': 'short description',
    }
    rule_result = rule.run(view)
    assert rule_result == False
