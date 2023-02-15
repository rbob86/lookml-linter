from linter.rule import Severity
from linter.rules.explore_tag_requires_owner import ExploreTagRequiresOwner


def test_run_method_successfully_validates_explore_tag_has_owner() -> None:
    rule = ExploreTagRequiresOwner(Severity.ERROR.value)

    explore = {
        'label': 'Aggregated User Data',
        'joins': [
            {
                'type': 'left_outer',
                'sql_always_where': '${created_date} >= "2017-01-01"',
                'sql_on': '${users_dt.user_id} = ${users.id}',
                'relationship': 'many_to_one',
                'name': 'users',
            }
        ],
        'name': 'users_dt',
        'tags': ['owner:jon_snow', 'PII data']
    }
    rule_result = rule.run(explore)
    assert rule_result == True


def test_run_method_fails_with_explore_tag_has_no_owner() -> None:
    rule = ExploreTagRequiresOwner(Severity.ERROR.value)

    explore = {
        'joins': [
            {
                'type': 'left_outer',
                'sql_always_where': '${created_date} >= "2017-01-01"',
                'sql_on': '${users_dt.user_id} = ${users.id}',
                'relationship': 'many_to_one',
                'name': 'users',
            }
        ],
        'name': 'users_dt',
        'tags': ['confidential', 'PII data']
    }
    rule_result = rule.run(explore)
    assert rule_result == False