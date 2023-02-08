from linter.rule import Severity
from linter.rules.field_name_is_snake_case import FieldNameIsSnakeCase


def test_run_method_successfully_validates_field_name_is_snake_case() -> None:
    rule = FieldNameIsSnakeCase(Severity.ERROR.value)

    field = {
        "name": "order_id",
        "primary_key": "yes",
        "sql": '${TABLE}."ORDER_ID"',
        "type": "number",
    }
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_field_name_is_not_snake_case() -> None:
    rule = FieldNameIsSnakeCase(Severity.ERROR.value)

    field = {
        "name": "OrderID",
        "primary_key": "yes",
        "sql": '${TABLE}."ORDER_ID"',
        "type": "number",
    }
    rule_result = rule.run(field)
    assert rule_result == False
