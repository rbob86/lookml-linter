from linter.rule import Severity
from linter.rules.explore_requires_description import ExploreRequiresDescription


def test_run_method_successfully_validates_explore_with_description() -> None:
    rule = ExploreRequiresDescription(Severity.ERROR.value)

    explore = {'sql_always_where': '1=1',
               'name': 'sku', 'description': 'testing'}
    rule_result = rule.run(explore)
    assert rule_result == True


def test_run_method_fails_with_explore_without_descriptions() -> None:
    rule = ExploreRequiresDescription(Severity.ERROR.value)

    explore = {'sql_always_where': '1=1',
               'name': 'sku', 'join': 'testing'}
    rule_result = rule.run(explore)
    assert rule_result == False
