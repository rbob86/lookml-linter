import sys

from linter.lookml_linter import LookMlLinter
from linter.rule_config_parser import RuleConfigParser


data = {
    "views": [
        {
            "derived_table": {
                "sql": "-- raw sql results do not include filled-in values for 'process_tats_rank.outflow_event_at_month'\n\n\n      WITH process_tats_rank AS (WITH event_raw AS (SELECT act.activity_id,\n                                act.loan_file_id,\n                                act.name       AS activity_name,\n                                act.is_deleted,\n                                act.title      AS activiy_title,\n                                act.created_at AS created_at,\n                                ast.created_at AS event_at,\n                                ast.account_id AS account_id,\n                                ast.to_status  AS event\n                         FROM core.activities act\n                                  JOIN clean.prod__activity_status_transition ast ON ast.activity_id = act.activity_id\n\n\n                         UNION\n\n                         SELECT act.activity_id,\n                             act.loan_file_id,\n                             act.name AS activity_name,\n                             act.is_deleted,\n                             act.title AS activiy_title,\n                             act.created_at AS created_at,\n                             asbt.created_at AS event_at,\n                             asbt.account_id AS account_id,\n                             asbt.to_substate AS EVENT\n                         FROM core.activities act\n                             JOIN clean.prod__activity_substate_transition asbt\n                         ON asbt.activity_id = act.activity_id),\n\n           inflow AS (SELECT activity_id                                                                                                                                       AS inflow_activity_id,\n                             loan_file_id,\n                             activity_name                                                                                                                                     AS inflow_activity_name,\n                             activiy_title                                                                                                                                     AS inflow_activity_title,\n                             is_deleted                                                                                                                                        AS inflow_is_deleted,\n                             created_at                                                                                                                                        AS inflow_created_at,\n                             event_at                                                                                                                                          AS inflow_event_at,\n                             account_id                                                                                                                                        AS inflow_account_id,\n                             event                                                                                                                                             AS inflow_event,\n                             row_number() OVER (PARTITION BY event_raw.loan_file_id ORDER BY event_at  ASC\n                                      ) AS inflow_event_rank\n                      FROM event_raw\n                      WHERE event_raw.event != 'Hidden'\n                        AND (event_raw.event = 'Finished')\n                        AND (event_raw.activity_name LIKE '%ProvideDesiredClosingDate%' OR event_raw.activity_name LIKE '%ProvideDesiredClosingDateV%')\n                        AND 1=1 -- no filter on 'process_tats_rank.inflow_activity_title'\n\n                        AND NOT COALESCE( event_raw.is_deleted , FALSE)),\n\n           outflow AS (SELECT activity_id                                                                                                                          AS outflow_activity_id,\n                              loan_file_id,\n                              activity_name                                                                                                                        AS outflow_activity_name,\n                              activiy_title                                                                                                                        AS outflow_activity_title,\n                              is_deleted                                                                                                                           AS outflow_is_deleted,\n                              created_at                                                                                                                           AS outflow_created_at,\n                              event_at                                                                                                                             AS outflow_event_at,\n                              account_id                                                                                                                           AS outflow_account_id,\n                              event                                                                                                                                AS outflow_event,\n                              row_number() OVER (PARTITION BY event_raw.loan_file_id ORDER BY event_raw.event_at  ASC\n                                      ) AS outflow_event_rank\n                       FROM event_raw\n                       WHERE event_raw.event != 'Hidden'\n                         AND (event_raw.event = 'Finished')\n                         AND (event_raw.activity_name ILIKE '%shareclosingdetailswithsettlementagent%')\n                         AND 1=1 -- no filter on 'process_tats_rank.outflow_activity_title'\n\n                         AND NOT COALESCE( event_raw.is_deleted , FALSE))\n\n      SELECT  inflow.*,\n              outflow.outflow_activity_id,\n              outflow.outflow_activity_name,\n              outflow.outflow_activity_title,\n              outflow.outflow_is_deleted,\n              outflow.outflow_created_at,\n              outflow.outflow_event_at,\n              outflow.outflow_account_id,\n              outflow.outflow_event\n      FROM inflow\n               JOIN outflow ON inflow.loan_file_id = outflow.loan_file_id\n              AND inflow.inflow_event_rank = 1\n              AND outflow.outflow_event_rank = 1)\n      SELECT\n          (TO_CHAR(DATE_TRUNC('month', process_tats_rank.outflow_event_at::timestamp ), 'YYYY-MM')) AS \"process_tats_rank.outflow_event_at_month\",\n          MEDIAN((date_diff('hours', (TO_CHAR(DATE_TRUNC('second', process_tats_rank.inflow_event_at::timestamp ), 'YYYY-MM-DD HH24:MI:SS'))::timestamp, (TO_CHAR(DATE_TRUNC('second', process_tats_rank.outflow_event_at::timestamp ), 'YYYY-MM-DD HH24:MI:SS'))::timestamp)/24.0)) AS \"median_of_tat\"\n      FROM process_tats_rank\n      LEFT JOIN core.loan_files  AS loan_files ON process_tats_rank.loan_file_id = loan_files.loan_file_id\n      WHERE ((( process_tats_rank.outflow_event_at::timestamp  ) >= ((DATEADD(month,-5, DATE_TRUNC('month', DATE_TRUNC('day',GETDATE())) ))) AND ( process_tats_rank.outflow_event_at::timestamp  ) < ((DATEADD(month,6, DATEADD(month,-5, DATE_TRUNC('month', DATE_TRUNC('day',GETDATE())) ) ))))) AND (loan_files.funnel ) = 'Refinance' AND (loan_files.tenant ) = 'Ally'\n      GROUP BY\n          (DATE_TRUNC('month', process_tats_rank.outflow_event_at::timestamp ))\n      ORDER BY\n          1 DESC\n      LIMIT 500"
            },
            "measures": [
                {"type": "count", "drill_fields": ["detail*"], "name": "count"}
            ],
            "dimensions": [
                {
                    "type": "string",
                    "sql": '${TABLE}."process_tats_rank.outflow_event_at_month"',
                    "name": "process_tats_rank_outflow_event_at_month",
                },
                {
                    "type": "number",
                    "sql": "${TABLE}.median_of_tat",
                    "name": "median_of_tat",
                },
            ],
            "sets": [
                {
                    "fields": [
                        "process_tats_rank_outflow_event_at_month",
                        "median_of_tat",
                    ],
                    "name": "detail",
                }
            ],
            "name": "shareclosingdetailswithsettlementagent_tat",
        }
    ]
}


def main():
    args = sys.argv[1:]

    if len(args) > 0:
        config_file = args[0]
        rules = RuleConfigParser(config_file).parse()
        LookMlLinter(data, rules).run()


main()
