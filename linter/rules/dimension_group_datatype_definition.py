from linter.rule import Rule
from linter.severity import Severity


class DimensionGroupDataTypeDefinition(Rule):
    def default_severity():
        return Severity.WARNING.value

    def applies_to():
        return ('dimension_group')

    def run(self, field):
        return