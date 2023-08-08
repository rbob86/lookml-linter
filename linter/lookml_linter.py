
from typing import Dict, List, TypedDict
from linter.rule import Rule, Severity


class RuleEngineType(TypedDict):
    name: str
    instance: Rule


class LookMlLinter:
    def __init__(self, data: Dict, rules: Dict[str, List[RuleEngineType]]) -> None:
        self.data = data
        self.rules = rules
        self.has_errors = False
        self.sql_table_names = {}

    def run(self) -> None:
        self._errors = []
        for filename in self.data:
            file_data = self.data[filename]
            views = file_data.get('views', [])
            explores = file_data.get('explores', [])
            includes = file_data.get('includes', [])
            self._errors.append({
                'filename': filename,
                'messages': []
            })
            for i in includes:
                self.__lint_object({'name': i}, 'include')
            for e in explores:
                self.__lint_object(e, 'explore')
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

    def get_errors(self) -> str:
        output = ''
        for error in self._errors:
            output += error['filename']
            if len(error['messages']) == 0:
                output += f'\n    No linting warnings/errors found.'
            error['messages'].sort(reverse=True)
            for message in error['messages']:
                output += f'\n    {message}'
            output += '\n'
        return output

    def save_errors(self, output: str, filename: str) -> None:
        f = open(filename, 'w')
        f.write(output)
        f.close()

    def __lint_object(self, object: Dict, object_type: str) -> None:
        for rule in self.rules.get(object_type, []):
            runner = rule['instance']
            if rule['name'] == 'view_must_have_unique_sql_table_name':
                success = runner.run(object, self.sql_table_names)
            else:
                success = runner.run(object)
            if not success:
                if not self.has_errors and runner.severity == 'error':
                    self.has_errors = True
                formatted_severity = self._format_severity(runner.severity)
                error_msg = f'{formatted_severity}: {object_type} {object["name"]} - {rule["name"]}'
                self._errors[-1]['messages'].append(error_msg)

    def _format_severity(self, severity: Severity) -> str:
        if severity == Severity.ERROR.value:
            return '🚨 **Error**'
        if severity == Severity.WARNING.value:
            return '**Warning**'
