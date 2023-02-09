from linter.rule import Severity
from linter.rules.yesno_field_name_must_start_with_is_or_has import YesnoFieldNameMustStartWithIsOrHas


def test_run_method_successfully_validates_yesno_dimension_name_starts_with_is_or_has() -> None:
    rule = YesnoFieldNameMustStartWithIsOrHas(Severity.ERROR.value)

    field = {
        'description': 'Was this flight diverted?',
        'name': 'is_diverted',
        'sql': '${TABLE}.diverted',
        'type': 'yesno'
    }
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_yesno_dimension_name_does_not_start_with_is_or_has() -> None:
    rule = YesnoFieldNameMustStartWithIsOrHas(Severity.ERROR.value)

    field = {
        'name': 'diverted',
        'sql': '${TABLE}.diverted',
        'type': 'yesno'
    }
    rule_result = rule.run(field)
    assert rule_result == False