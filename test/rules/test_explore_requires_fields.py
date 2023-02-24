from linter.rule import Severity
from linter.rules.explore_requires_fields import ExploreRequiresFields


def test_run_method_successfully_validates_explore_with_fields() -> None:
    rule = ExploreRequiresFields(Severity.ERROR.value)

    explore = {
        'label': 'Carrier Information',
        'fields': ['ALL_FIELDS*'],
        'name': 'carrier'
    }
    rule_result = rule.run(explore)
    assert rule_result == True


def test_run_method_fails_explore_without_fields() -> None:
    rule = ExploreRequiresFields(Severity.ERROR.value)

    explore = {
        'label': 'Carrier Information',
        'name': 'carrier'
    }
    rule_result = rule.run(explore)
    assert rule_result == False