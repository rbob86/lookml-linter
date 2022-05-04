from rules.rule import Rule


class FieldShouldHaveDescription(Rule):
    def run(self, field):
        if not 'description' in field:
            return False
        return True
