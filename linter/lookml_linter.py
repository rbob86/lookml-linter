
from typing import Dict, List, TypedDict
from linter.helpers import pascal_case_to_snake_case
from linter.rule import Rule, Severity


class RuleEngineType(TypedDict):
    name: str
    instance: Rule


class LookMlLinter:
    def __init__(self, data: Dict, rules: Dict[str, List[RuleEngineType]]) -> None:
        self.data = data
        self.rules = rules
        self.linter_severity_status = True

    def run(self) -> None:
        self._errors = []

        for filename in self.data:
            file_data = self.data[filename]
            views = file_data.get('views', [])
            explores = file_data.get('explores', [])
            self._errors.append({
                'filename': filename,
                'messages': []
            })

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

    def print_errors(self) -> None:
        for error in self._errors:
            print(error['filename'])
            if len(error['messages']) == 0:
                print(f'    No linting warnings/errors found.')
            for message in error['messages']:
                print(f'    {message}')
            print()

    def __lint_object(self, object: Dict, object_type: str) -> None:
        if object_type in self.rules:
            for rule in self.rules[object_type]:
                runner = rule['instance']
                if runner.severity != Severity.IGNORE.value:
                    success = runner.run(object)
                    if not success:
                        if runner.severity == 'error' and self.linter_severity_status:
                            self.linter_severity_status = False
                        error_msg = f'{runner.severity}: {object_type} {object["name"]} - {rule["name"]}'
                        self._errors[-1]['messages'].append(error_msg)
