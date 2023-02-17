from linter.rule import Severity
from linter.rules.model_file_should_not_have_wildcard_view_includes import ModelFileShouldNotHaveWildcardViewIncludes


def test_run_method_successfully_validates_model_has_no_wildcard_view_includes() -> None:
    rule = ModelFileShouldNotHaveWildcardViewIncludes(Severity.ERROR.value)

    explore = {
        'includes': ['/views/**/orders.view',
                     '/dashboard/*.dashboard',
                     '/explores/*.explore.lkml'],
        'joins': [{'name': 'users',
                   'relationship': 'many_to_one',
                   'sql_on': '${orders.user_id} = ${users.id}',
                   'type': 'left_outer'}],
        'label': 'Order Details',
        'name': 'orders'
    }
    rule_result = rule.run(explore)
    assert rule_result == True


def test_run_method_fails_model_with_wildcard_include() -> None:
    rule = ModelFileShouldNotHaveWildcardViewIncludes(Severity.ERROR.value)

    explore = {
        'includes': ['/views/**/*.view',
                     '/dashboard/*.dashboard',
                     '/explores/*.explore.lkml'],
        'joins': [{'name': 'users',
                   'relationship': 'many_to_one',
                   'sql_on': '${orders.user_id} = ${users.id}',
                   'type': 'left_outer'}],
        'label': 'Order Details',
        'name': 'orders'
    }
    rule_result = rule.run(explore)
    assert rule_result == False
