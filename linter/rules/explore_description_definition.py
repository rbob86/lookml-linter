from linter.rule import Rule
from linter.severity import Severity


class ExploreDescriptionDefinition(Rule):
    def default_severity():
        return Severity.ERROR.value

    def applies_to():
        return ('explore',)

    def run(self, explore):
        if not 'description' in explore:
            return False
        return True