from linter.severity import Severity
from linter.rule import Rule


class ViewShouldHaveZ(Rule):
    def default_severity():
        return Severity.ERROR.value

    def applies_to():
        return ('view',)

    def run(self, view):
        return True
