
from typing import Dict, List
from linter.rule import Rule
from linter.severity import Severity


class LookMlLinter:
    def __init__(self, data: Dict, rules: Dict[str, List[Rule]]) -> None:
        self.data = data
        self.rules = rules

    def run(self) -> None:
        for file in self.data:
            file_data = self.data[file]
            views = file_data.get('views', [])
            explores = file_data.get('explores', [])

            for v in views:
                self.__lint_object(v, 'view')
                dimensions, measures, dimension_groups = [
                    v.get(key, []) for key in ['dimensions', 'measures', 'dimension_groups']]
                for d in dimensions:
                    self.__lint_object(d, 'dimension')
                for g in dimension_groups:
                    self.__lint_object(g, 'dimension_group')
                for m in measures:
                    self.__lint_object(m, 'measure')

            for e in explores:
                self.__lint_object(e, 'explore')

    def __lint_object(self, object: Dict, object_type: str) -> None:
        if object_type in self.rules:
            for rule in self.rules[object_type]:
                rule.run(object)
