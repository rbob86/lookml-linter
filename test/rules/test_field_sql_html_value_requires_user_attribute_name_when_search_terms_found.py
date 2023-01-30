# from linter.rule import Severity
# from linter.rules.field_sql_html_requires_user_attribute_when_search_terms_found_exact import FieldSqlHtmlRequiresUserAttributeWhenSearchTermsFoundExact


# def test_run_method_successfully_validates_field_with_search_term_hits_and_user_attributes_permissions() -> None:
#     params = {
#         'user_attribute': 'permissions_financial_row_level',
#         'search_terms': ['id']
#     }
#     rule = FieldSqlHtmlRequiresUserAttributeWhenSearchTermsFoundExact(
#         Severity.ERROR.value, params)
#     field = {'primary_key': 'yes', 'type': 'number', 'sql': 'CASE WHEN {{ _user_attributes[""permissions_financial_row_level""] }} = 1 THEN\n            ${TABLE}.id\n        ELSE\n            -1\n        END',
#              'html': '{% if _user_attributes[""permissions_financial_row_level""] == 1 %}\n        {{ rendered_value }}\n        {% else %}\n        [Insufficient Permissions]\n        {% endif %}', 'name': 'id', 'labsel': 'test'}
#     rule_result = rule.run(field)
#     assert rule_result == True


# def test_run_method_fails_field_with_search_term_hits_and_no_user_attributes_permissions() -> None:
#     params = {
#         'user_attribute': 'permissions_financial_row_level',
#         'search_terms': ['id']
#     }
#     rule = FieldSqlHtmlRequiresUserAttributeWhenSearchTermsFoundExact(
#         Severity.ERROR.value, params)
#     field = {'primary_key': 'yes', 'type': 'number', 'sql': 'CASE WHEN {{ _user_attributes[""permissions_financial_row_level""] }} = 1 THEN\n            ${TABLE}.id\n        ELSE\n            -1\n        END',
#              'html': '{% if ""permissions_financial_row_level"" == 1 %}\n        {{ rendered_value }}\n        {% else %}\n        [Insufficient Permissions]\n        {% endif %}', 'name': 'id'}
#     rule_result = rule.run(field)
#     assert rule_result == False


# def test_run_method_fails_field_with_search_term_hits_and_no_html_paramater() -> None:
#     params = {
#         'user_attribute': 'permissions_financial_row_level',
#         'search_terms': ['id', 'keys']
#     }
#     rule = FieldSqlHtmlRequiresUserAttributeWhenSearchTermsFoundExact(
#         Severity.ERROR.value, params)
#     field = {'primary_key': 'yes', 'type': 'number', 'name': 'id',
#              'sql': 'CASE WHEN {{ _user_attributes[""permissions_financial_row_level""] }} = 1 THEN\n            ${TABLE}.id\n        ELSE\n            -1\n        END'}
#     rule_result = rule.run(field)
#     assert rule_result == False


# def test_run_method_fails_field_with_no_search_term_hits() -> None:
#     params = {
#         'user_attribute': 'permissions_financial_row_level',
#         'search_terms': ['keys']
#     }
#     rule = FieldSqlHtmlRequiresUserAttributeWhenSearchTermsFoundExact(
#         Severity.ERROR.value, params)
#     field = {'primary_key': 'yes', 'type': 'number', 'sql': 'CASE WHEN {{ _user_attributes[""permissions_financial_row_level""] }} = 1 THEN\n            ${TABLE}.id\n        ELSE\n            -1\n        END',
#              'html': '{% if ""permissions_financial_row_level"" == 1 %}\n        {{ rendered_value }}\n        {% else %}\n        [Insufficient Permissions]\n        {% endif %}', 'name': 'id'}
#     rule_result = rule.run(field)
#     assert rule_result == True
