from linter.rule import Severity
from linter.rules.primary_key_is_first_dimension_in_view import PrimaryKeyIsFirstDimensionInView
from linter.rules.primary_key_prefix_and_is_hidden import PrimaryKeyPrefixAndIsHidden


def test_run_method_successfully_validates_primary_key_prefix_and_is_hidden() -> None:
    rule = PrimaryKeyPrefixAndIsHidden(Severity.ERROR.value)

    dimension = {
        'name': 'pk_id',
        'primary_key': 'yes',
        'sql': '${TABLE}.ID',
        'type': 'number',
        'hidden': 'yes'
    }

    rule_result = rule.run(dimension)
    assert rule_result == True


def test_run_method_fails_when_primary_key_is_not_hidden() -> None:
    rule = PrimaryKeyPrefixAndIsHidden(Severity.ERROR.value)

    dimension = {
        'name': 'id',
        'primary_key': 'yes',
        'sql': '${TABLE}.ID',
        'type': 'number',
    }

    rule_result = rule.run(dimension)
    assert rule_result == False

def test_run_method_fails_when_primary_key_does_not_start_with_pk() -> None:
    rule = PrimaryKeyPrefixAndIsHidden(Severity.ERROR.value)

    dimension = {
        'name': 'id',
        'primary_key': 'yes',
        'sql': '${TABLE}.ID',
        'type': 'number',
    }

    rule_result = rule.run(dimension)
    assert rule_result == False
