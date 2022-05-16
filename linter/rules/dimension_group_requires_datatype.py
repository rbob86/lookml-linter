from linter.rule import Rule
from linter.severity import Severity


class DimensionGroupRequiresDataType(Rule):
    def default_severity():
        return Severity.WARNING.value

    def applies_to():
        return ('dimension_group',)

    def run(self, dimension_group):
        if not 'datatype' in dimension_group:
            return False
        return True