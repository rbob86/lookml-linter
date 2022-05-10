import pytest
from linter.severity import Severity
from linter.rule_factory import RuleFactory
from linter.rule_names import RuleNames


def test_build_method_throws_key_error_if_rule_class_does_not_exist() -> None:
    factory = RuleFactory()
    for rule_name in RuleNames.get():
        rule_name = rule_name + '--invalid'
        with pytest.raises(KeyError):
            factory.build(rule_name)


def test_build_method_returns_appropriate_rule() -> None:
    factory = RuleFactory()
    for rule_name in RuleNames.get():
        rule = factory.build(rule_name)
        rule_class_name = type(rule).__name__
        class_name = factory._RuleFactory__rule_name_to_classname(rule_name)
        assert rule_class_name == class_name


def test_build_method_returns_rule_with_correct_severity() -> None:
    factory = RuleFactory()
    for rule_name in RuleNames.get():
        rule = factory.build(rule_name)
        rule_class = rule.__class__
        assert rule.severity == rule_class.default_severity()
        rule = factory.build(rule_name, Severity.IGNORE.value)
        assert rule.severity == Severity.IGNORE.value
        rule = factory.build(rule_name, Severity.WARNING.value)
        assert rule.severity == Severity.WARNING.value
