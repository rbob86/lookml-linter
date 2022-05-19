from linter.rule import Severity
from linter.rules.field_requires_description import FieldRequiresDescription


def test_run_method_successfully_validates_field_with_description() -> None:
    rule = FieldRequiresDescription(Severity.ERROR.value)

    field = {'type': 'string', 'sql': '${TABLE}.sku',
             'name': 'sku', 'description': 'testing'}
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_with_field_without_descriptions() -> None:
    rule = FieldRequiresDescription(Severity.ERROR.value)

    field = {'type': 'string', 'sql': '${TABLE}.sku',
             'name': 'sku'}
    rule_result = rule.run(field)
    assert rule_result == False
