from linter.helpers import snake_case_to_pascal_case
import pytest
from linter.rule import Severity
from linter.rule_factory import RuleFactory
from linter.rules_engine import RulesEngine


def test_build_method_throws_key_error_if_rule_class_does_not_exist() -> None:
    factory = RuleFactory()
    for rule_name in RulesEngine.rule_names():
        rule_name = rule_name + '--invalid'
        with pytest.raises(KeyError):
            factory.build(rule_name, Severity.ERROR.value)


def test_build_method_returns_appropriate_rule() -> None:
    factory = RuleFactory()
    for rule_name in RulesEngine.rule_names():
        rule = factory.build(rule_name, Severity.ERROR.value)
        rule_class_name = type(rule).__name__
        class_name = snake_case_to_pascal_case(rule_name)
        assert rule_class_name == class_name


def test_build_method_returns_rule_with_correct_severity() -> None:
    factory = RuleFactory()
    for rule_name in RulesEngine.rule_names():
        rule = factory.build(rule_name, Severity.IGNORE.value)
        assert rule.severity == Severity.IGNORE.value
        rule = factory.build(rule_name, Severity.WARNING.value)
        assert rule.severity == Severity.WARNING.value
