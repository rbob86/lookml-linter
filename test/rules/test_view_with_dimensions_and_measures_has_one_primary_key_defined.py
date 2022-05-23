from linter.rule import Severity
from linter.rules.view_with_dimensions_and_measures_has_one_primary_key import ViewWithDimensionsAndMeasuresHasOnePrimaryKey


def test_run_method_successfully_validates_view_file_with_dimensions_and_measures_has_one_primary_key() -> None:
    rule = ViewWithDimensionsAndMeasuresHasOnePrimaryKey(
        Severity.ERROR.value)

    view = {'sql_table_name': 'public.products', 'dimensions': [{'primary_key': 'yes', 'type': 'number', 'sql': 'CASE WHEN {{ _user_attributes[""permissions_financial_row_level""] }} = 1 THEN\n            ${TABLE}.id\n        ELSE\n            -1\n        END',
                                                                 'html': '{% if _user_attributes[""permissions_financial_row_level""] == 1 %}\n        {{ rendered_value }}\n        {% else %}\n        [Insufficient Permissions]\n        {% endif %}', 'name': 'id'}], 'name': 'products'}
    rule_result = rule.run(view)
    assert rule_result == True


def test_run_method_successfully_validates_view_file_with_dimensions_and_no_measures_does_not_require_primary_key() -> None:
    rule = ViewWithDimensionsAndMeasuresHasOnePrimaryKey(
        Severity.ERROR.value)

    view = {'sql_table_name': 'public.products',
            'dimensions': range(0, 50), 'name': 'total_cost'}
    rule_result = rule.run(view)
    assert rule_result == True


def test_run_method_successfully_validates_view_file_with_no_dimensions_and_measures_does_not_require_primary_key() -> None:
    rule = ViewWithDimensionsAndMeasuresHasOnePrimaryKey(
        Severity.ERROR.value)

    view = {'sql_table_name': 'public.products',
            'measure': range(0, 50), 'name': 'total_cost'}
    rule_result = rule.run(view)
    assert rule_result == True


def test_run_method_fails_when_view_with_dimensions_and_measures_does_not_have_a_primary_key() -> None:
    rule = ViewWithDimensionsAndMeasuresHasOnePrimaryKey(
        Severity.ERROR.value)

    view = {'sql_table_name': 'public.products',
            'dimensions': [str(dim) for dim in range(0, 50)], 'name': 'this_view',
            'measures': [str(measure) for measure in range(0, 50)]}
    rule_result = rule.run(view)
    assert rule_result == False
