from linter.rule import Rule
from linter.severity import Severity


class FieldRequiresDescription(Rule):
    def default_severity():
        return Severity.ERROR.value

    def applies_to():
        return ('dimension', 'measure')

    def run(self, field):
        if not 'description' in field:
            return False
        return True
