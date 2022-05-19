from linter.rules.field_sql_html_value_requires_user_attribute_name_when_search_terms_found import FieldSqlHtmlValueRequiresUserAttributeNameWhenSearchTermsFound


def test_run_method_successfully_validates_field_with_search_term_hits_and_user_attributes_permissions() -> None:
    rule = FieldSqlHtmlValueRequiresUserAttributeNameWhenSearchTermsFound()

    field = {'primary_key': 'yes', 'type': 'number', 'sql': 'CASE WHEN {{ _user_attributes[""permissions_financial_row_level""] }} = 1 THEN\n            ${TABLE}.id\n        ELSE\n            -1\n        END',
             'html': '{% if _user_attributes[""permissions_financial_row_level""] == 1 %}\n        {{ rendered_value }}\n        {% else %}\n        [Insufficient Permissions]\n        {% endif %}', 'name': 'id'}
    search_terms = ['id', 'keys']
    user_attribute = 'permissions_financial_row_level'
    rule_result = rule.run(field, user_attribute, search_terms)
    assert rule_result == True


def test_run_method_fails_field_with_search_term_hits_and_no_user_attributes_permissions() -> None:
    rule = FieldSqlHtmlValueRequiresUserAttributeNameWhenSearchTermsFound()

    field = {'primary_key': 'yes', 'type': 'number', 'sql': 'CASE WHEN {{ _user_attributes[""permissions_financial_row_level""] }} = 1 THEN\n            ${TABLE}.id\n        ELSE\n            -1\n        END',
             'html': '{% if ""permissions_financial_row_level"" == 1 %}\n        {{ rendered_value }}\n        {% else %}\n        [Insufficient Permissions]\n        {% endif %}', 'name': 'id'}
    search_terms = ['id', 'keys']
    user_attribute = 'permissions_financial_row_level'
    rule_result = rule.run(field, user_attribute, search_terms)
    assert rule_result == False


def test_run_method_fails_field_with_search_term_hits_and_no_html_paramater() -> None:
    rule = FieldSqlHtmlValueRequiresUserAttributeNameWhenSearchTermsFound()

    field = {'primary_key': 'yes', 'type': 'number', 'name': 'id',
             'sql': 'CASE WHEN {{ _user_attributes[""permissions_financial_row_level""] }} = 1 THEN\n            ${TABLE}.id\n        ELSE\n            -1\n        END'}
    search_terms = ['id', 'keys']
    user_attribute = 'permissions_financial_row_level'
    rule_result = rule.run(field, user_attribute, search_terms)
    assert rule_result == False


def test_run_method_fails_field_with_no_search_term_hits() -> None:
    rule = FieldSqlHtmlValueRequiresUserAttributeNameWhenSearchTermsFound()

    field = {'primary_key': 'yes', 'type': 'number', 'sql': 'CASE WHEN {{ _user_attributes[""permissions_financial_row_level""] }} = 1 THEN\n            ${TABLE}.id\n        ELSE\n            -1\n        END',
             'html': '{% if ""permissions_financial_row_level"" == 1 %}\n        {{ rendered_value }}\n        {% else %}\n        [Insufficient Permissions]\n        {% endif %}', 'name': 'id'}
    search_terms = ['keys']
    user_attribute = 'permissions_financial_row_level'
    rule_result = rule.run(field, user_attribute, search_terms)
    assert rule_result == True
