from linter.rule import Severity
from linter.rules.explore_requires_label import ExploreRequiresLabel


def test_run_method_successfully_validates_explore_with_label() -> None:
    rule = ExploreRequiresLabel(Severity.ERROR.value)

    explore = {
        "label": "Aggregated User Data",
        "joins": [
            {
                "type": "left_outer",
                "sql_always_where": "${created_date} >= '2017-01-01'",
                "sql_on": "${users_dt.user_id} = ${users.id}",
                "relationship": "many_to_one",
                "name": "users",
            }
        ],
        "name": "users_dt",
    }
    rule_result = rule.run(explore)
    assert rule_result == True


def test_run_method_fails_with_explore_without_label() -> None:
    rule = ExploreRequiresLabel(Severity.ERROR.value)

    explore = {
        "joins": [
            {
                "type": "left_outer",
                "sql_always_where": "${created_date} >= '2017-01-01'",
                "sql_on": "${users_dt.user_id} = ${users.id}",
                "relationship": "many_to_one",
                "name": "users",
            }
        ],
        "name": "users_dt",
    }
    rule_result = rule.run(explore)
    assert rule_result == False