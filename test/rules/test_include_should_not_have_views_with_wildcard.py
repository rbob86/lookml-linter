from linter.rule import Severity
from linter.rules.include_should_not_have_views_with_wildcard import IncludeShouldNotHaveViewsWithWildcard


def test_run_method_successfully_validates_include_has_no_wildcard_view() -> None:
    rule = IncludeShouldNotHaveViewsWithWildcard(Severity.ERROR.value)

    include = {'name': '/views/**/orders.view'}
    rule_result = rule.run(include)
    assert rule_result == True


def test_run_method_fails_include_with_wildcard_view() -> None:
    rule = IncludeShouldNotHaveViewsWithWildcard(Severity.ERROR.value)

    include = {'name': '/views/**/*.view'}
    rule_result = rule.run(include)
    assert rule_result == False
