from linter.rule import Rule
from linter.severity import Severity


class ExploreDescriptionDefinition(Rule):
    def default_severity():
        return Severity.ERROR.value

    def applies_to():
        return ('explore')

    def run(self, field):
        if not 'description' in field:
            return False
        return True