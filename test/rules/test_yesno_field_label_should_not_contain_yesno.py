from linter.rule import Severity
from linter.rules.yesno_field_label_should_not_contain_yesno import YesnoFieldLabelShouldNotContainYesno


def test_run_method_successfully_validates_yesno_label_does_not_contain_yesno() -> None:
    rule = YesnoFieldLabelShouldNotContainYesno(Severity.ERROR.value)

    field = {'label': 'Is this on time?',
             'name': 'is_on_time', 'type': 'yesno'}
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_when_yesno_label_contains_yesno() -> None:
    rule = YesnoFieldLabelShouldNotContainYesno(Severity.ERROR.value)

    field = {'label': 'Is this valid (Yes/no)?',
             'name': 'is_valid', 'type': 'yesno'}
    rule_result = rule.run(field)
    assert rule_result == False
