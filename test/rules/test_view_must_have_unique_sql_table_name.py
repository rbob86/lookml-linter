from linter.rule import Severity
from linter.rules.view_must_have_unique_sql_table_name import ViewMustHaveUniqueSqlTableName


def test_run_method_successfully_validates_unique_sql_table_names() -> None:
    rule = ViewMustHaveUniqueSqlTableName(Severity.ERROR.value)
    rule_result1 = rule.run({'sql_table_name': 'table_name'}, {})
    rule_result2 = rule.run({'sql_table_name': 'another_table_name'}, {'table_name': 1})
    assert rule_result1 == True and rule_result2 == True


def test_run_method_fails_on_non_unique_sql_table_names() -> None:
    rule = ViewMustHaveUniqueSqlTableName(Severity.ERROR.value)
    rule_result1 = rule.run({'sql_table_name': 'table_name'}, {})
    rule_result2 = rule.run({'sql_table_name': 'table_name'}, {'table_name': 1})
    rule_result3 = rule.run({'sql_table_name': 'another_table_name'}, {'table_name': 1})
    rule_result4 = rule.run({'sql_table_name': 'table_name'}, {'table_name': 1, 'another_table_name': 1})
    assert rule_result1 == True and rule_result2 == False and rule_result3 == True and rule_result4 == False