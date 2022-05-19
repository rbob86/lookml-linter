from linter.rule import Severity
from linter.rules.view_with_many_fields_requires_fields_hidden_by_default import ViewWithManyFieldsRequiresFieldsHiddenByDefault


def test_run_method_successfully_validates_empty_view_file() -> None:
    rule = ViewWithManyFieldsRequiresFieldsHiddenByDefault(
        Severity.ERROR.value)

    view = {}
    rule_result = rule.run(view)
    assert rule_result == True


def test_run_method_successfully_validates_view_file_with_less_than_50_fields() -> None:
    rule = ViewWithManyFieldsRequiresFieldsHiddenByDefault(
        Severity.ERROR.value)

    view = {'sql_table_name': 'public.products', 'dimensions': [{'primary_key': 'yes', 'type': 'number', 'sql': 'CASE WHEN {{ _user_attributes[""permissions_financial_row_level""] }} = 1 THEN\n            ${TABLE}.id\n        ELSE\n            -1\n        END',
                                                                 'html': '{% if _user_attributes[""permissions_financial_row_level""] == 1 %}\n        {{ rendered_value }}\n        {% else %}\n        [Insufficient Permissions]\n        {% endif %}', 'name': 'id'}], 'name': 'products'}
    rule_result = rule.run(view)
    assert rule_result == True


def test_run_method_successfully_validates_view_file_with_more_than_50_fields() -> None:
    rule = ViewWithManyFieldsRequiresFieldsHiddenByDefault(
        Severity.ERROR.value)

    view = {'sql_table_name': 'public.products',
            'fields_hidden_by_default': "yes", 'dimensions': range(0, 50), 'name': 'total_cost'}
    rule_result = rule.run(view)
    assert rule_result == True


def test_run_method_fails_view_file_with_more_than_50_fields_if_fields_hidden_missing() -> None:
    rule = ViewWithManyFieldsRequiresFieldsHiddenByDefault(
        Severity.ERROR.value)

    view = {'sql_table_name': 'public.products',
            'dimensions': range(0, 50), 'name': 'total_cost'}
    rule_result = rule.run(view)
    assert rule_result == False
