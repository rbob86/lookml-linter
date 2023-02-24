from linter.rule import Severity
from linter.rules.explore_requires_always_filter import ExploreRequiresAlwaysFilter


def test_run_method_successfully_validates_explore_with_always_filter() -> None:
    rule = ExploreRequiresAlwaysFilter(Severity.ERROR.value)

    explore = {
        'always_filter': {'filters__all': [[{'code': '-NULL'}]]},
        'label': 'Carrier Information',
        'name': 'carrier'
    }
    rule_result = rule.run(explore)
    assert rule_result == True


def test_run_method_fails_explore_without_always_filter() -> None:
    rule = ExploreRequiresAlwaysFilter(Severity.ERROR.value)

    explore = {
        'label': 'Carrier Information',
        'name': 'carrier'
    }
    rule_result = rule.run(explore)
    assert rule_result == False