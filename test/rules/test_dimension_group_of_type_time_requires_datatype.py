from linter.rule import Severity
from linter.rules.dimension_group_of_type_time_requires_datatype import DimensionGroupOfTypeTimeRequiresDatatype


def test_run_method_successfully_validates_time_dimension_group_has_datatype() -> None:
    rule = DimensionGroupOfTypeTimeRequiresDatatype(Severity.ERROR.value)

    dimension_group = {'type': 'time', 'datatype': 'day'}
    rule_result = rule.run(dimension_group)
    assert rule_result == True


def test_run_method_fails_when_time_dimension_group_does_not_have_datatype() -> None:
    rule = DimensionGroupOfTypeTimeRequiresDatatype(Severity.ERROR.value)

    dimension_group = {'type': 'time'}
    rule_result = rule.run(dimension_group)
    assert rule_result == False
