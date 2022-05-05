# import pytest
from linter.ruleset import Ruleset, Severity
from linter.rules.view_should_have_z import ViewShouldHaveZ
from linter.rules.field_should_have_description import FieldShouldHaveDescription


def test_rules_property_names_correspond_to_existing_classes() -> None:
    rule_names = [rule['name'] for rule in Ruleset.rules]
    for rule_name in rule_names:
        classname = rule_name.replace('_', ' ').title().replace(' ', '')
        assert classname in globals()


def test_rules_to_apply_method_returns_all_rules_except_those_with_ignore_severity() -> None:
    rules = list(Ruleset.rules)
    rules.append({
        "name": "test_rule",
        "object_type": "dimension",
        "severity": Severity.IGNORE.value
    })
    Ruleset.rules = tuple(rules)

    new_rule_exists = False
    for rule in Ruleset.rules:
        if rule['name'] == 'test_rule':
            new_rule_exists = True
    assert new_rule_exists == True

    new_rule_exists = False
    for rule in Ruleset.rules_to_apply():
        if rule['name'] == 'test_rule':
            new_rule_exists = True
    assert new_rule_exists == False


def test_apply_severity_overrides_succesfully_applies_overrides_to_rules() -> None:
    pass


def test_apply_severity_overrides_method_throws_error_if_config_schema_invalid() -> None:
    pass


def test_apply_severity_overrides_method_throws_error_if_override_rule_name_invalid() -> None:
    pass


def test_apply_severity_overrides_method_throws_error_if_override_severity_invalid() -> None:
    pass
