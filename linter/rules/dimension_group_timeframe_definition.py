from linter.rule import Rule
from linter.severity import Severity


class DimensionGroupTimeframeDefinition(Rule):
    def default_severity():
        return Severity.WARNING.value

    def applies_to():
        return ('dimension_group')

    def run(self, dimension_group):
        if not 'timeframe' in dimension_group:
            return False
        return True