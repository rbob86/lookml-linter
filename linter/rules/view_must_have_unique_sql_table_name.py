from linter.rule import Rule
from typing import Any, Dict, Tuple


class ViewMustHaveUniqueSqlTableName(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('view',)

    def run(self, view: Any, sql_table_names: Dict[str, int]) -> bool:
        if 'sql_table_name' in view:
            if view['sql_table_name'] in sql_table_names:
                sql_table_names[view['sql_table_name']] = 1
                return False
            sql_table_names[view['sql_table_name']] = 1
        return True