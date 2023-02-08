from linter.rule import Severity
from linter.rules.view_name_is_snake_case import ViewNameIsSnakeCase


def test_run_method_successfully_validates_view_name_is_snake_case() -> None:
    rule = ViewNameIsSnakeCase(Severity.ERROR.value)

    view = {
        "dimensions": [
            {
                "name": "id",
                "primary_key": "yes",
                "sql": '${TABLE}."ID"',
                "type": "number",
            },
            {
                "name": "inventory_item_id",
                "sql": '${TABLE}."INVENTORY_ITEM_ID"',
                "type": "number",
            },
        ],
        "name": "order_items",
        "sql_table_name": '"PUBLIC"."ORDER_ITEMS"',
    }

    rule_result = rule.run(view)
    assert rule_result == True


def test_run_method_fails_view_name_is_not_snake_case() -> None:
    rule = ViewNameIsSnakeCase(Severity.ERROR.value)

    view = {
        "dimensions": [
            {
                "name": "id",
                "primary_key": "yes",
                "sql": '${TABLE}."ID"',
                "type": "number",
            },
            {
                "name": "inventory_item_id",
                "sql": '${TABLE}."INVENTORY_ITEM_ID"',
                "type": "number",
            },
        ],
        "name": "OrderItems",
        "sql_table_name": '"PUBLIC"."ORDER_ITEMS"',
    }

    rule_result = rule.run(view)
    assert rule_result == False
