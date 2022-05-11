from linter.severity import Severity
from linter.rule import Rule


class ViewShouldHaveZ(Rule):
    def default_severity():
        return Severity.ERROR.value

    def applies_to():
        return ('view',)


    # hidden by default should be toggled on
    # if there are over 50 fields in the view
    def ViewHiddenByDefault(self, view):
        dimensions, measures, dimension_groups = [
        view.get(key, []) for key in ['dimensions', 'measures', 'dimension_groups']]

        number_of_fields = len(dimension_groups) + len(measures) + len(dimensions)

        if number_of_fields >= 50 and not 'fields_hidden_by_default' in view:
            return False
        return True
