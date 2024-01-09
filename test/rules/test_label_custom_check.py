from linter.rule import Severity
from linter.rules.label_custom_check import LabelCustomCheck


def test_lookml_object_with_label() -> None:
    rule = LabelCustomCheck(Severity.ERROR.value)

    view = {
        'dimensions': {
            'user_name': {
                'type': 'string',
                'label': '(Non-VN) Used PayPal 2022 - Fees',
                'description': 'Name of User',
                'sql': '${TABLE}.USER_NAME'
            },
            'user_last_name': {
                'type': 'string',
                'label': ' Last Name', #e.g. Forcing order by adding space to label start
                'description': 'User Last Name',
                'sql': '${TABLE}.USER_LAST_NAME'
            },
            'user_id': {
                'type': 'string',
                'label': '   ',  # only whitespaces
                'description': 'User ID',
                'sql': '${TABLE}.USER_ID'
            },
            'requester_name': {
                'type': 'string',
                'label': '(requester)', # not in Camel Case
                'description': 'Name of User',
                'sql': '${TABLE}.USER_NAME'
            }
        },
        'label': 'Primary Sales Channel In 90D',
        'name': 'order_items',
        'sql_table_name': '"PUBLIC"."ORDER_ITEMS"'
    }
    rule_result = rule.run(view)
    assert rule_result == True

    rule_result = rule.run(view['dimensions']['user_name'])
    assert rule_result == True

    rule_result = rule.run(view['dimensions']['user_last_name'])
    assert rule_result == True

    rule_result = rule.run(view['dimensions']['user_id'])
    assert rule_result == False

    rule_result = rule.run(view['dimensions']['requester_name'])
    assert rule_result == False


def test_lookml_object_without_label() -> None:
    rule = LabelCustomCheck(Severity.ERROR.value)

    view = {
        'name': 'order_items',
        'sql_table_name': '"PUBLIC"."ORDER_ITEMS"'
    }
    rule_result = rule.run(view)
    assert rule_result == True