from linter.rule import Rule


class FieldRequiresDescription(Rule):
    def applies_to():
        return ('dimension', 'measure')

    def run(self, field):
        if not 'description' in field:
            return False
        return True
