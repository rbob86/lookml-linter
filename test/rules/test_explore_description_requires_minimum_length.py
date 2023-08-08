from linter.rule import Severity
from linter.rules.explore_description_requires_minimum_length import (
    ExploreDescriptionRequiresMinimumLength,
)


def test_run_method_successfully_validates_explore_with_minimum_length_description() -> (
    None
):
    params = {"min_length": 20}
    rule = ExploreDescriptionRequiresMinimumLength(Severity.ERROR.value, params)

    explore = {
        "sql_always_where": "1=1",
        "name": "sku",
        "description": "testing with a long description",
    }
    rule_result = rule.run(explore)
    assert rule_result == True


def test_run_method_successfully_validates_explore_without_description() -> None:
    params = {"min_length": 20}
    rule = ExploreDescriptionRequiresMinimumLength(Severity.ERROR.value, params)

    explore = {"sql_always_where": "1=1", "name": "sku"}
    rule_result = rule.run(explore)
    assert rule_result == True


def test_run_method_fails_with_explore_with_short_description() -> None:
    params = {"min_length": 20}
    rule = ExploreDescriptionRequiresMinimumLength(Severity.ERROR.value, params)

    explore = {"sql_always_where": "1=1", "name": "sku", "description": "testing"}
    rule_result = rule.run(explore)
    assert rule_result == False
