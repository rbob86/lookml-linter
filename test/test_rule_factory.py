import pytest
from linter.rule_factory import RuleFactory

rule_names = (
    'field_should_have_description',
    # 'dimension_should_have_x',
    # 'measure_should_have_y',
    'view_should_have_z',
    # 'view_requires_abc',
    # 'view_requires_xyz',
)


def test_build_method_throws_key_error_if_rule_class_does_not_exist() -> None:
    factory = RuleFactory()
    for rule_name in rule_names:
        rule_name = rule_name + '--invalid'
        with pytest.raises(KeyError):
            factory.build(rule_name)


def test_build_method_returns_appropriate_rule() -> None:
    factory = RuleFactory()
    for rule_name in rule_names:
        rule = factory.build(rule_name)
        rule_class_name = type(rule).__name__
        # get output of private method
        class_name = factory._RuleFactory__rule_name_to_classname(rule_name)
        assert rule_class_name == class_name
