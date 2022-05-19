from linter.rule import Rule


class ExploreRequiresDescription(Rule):
    def applies_to():
        return ('explore',)

    def run(self, explore):
        if not 'description' in explore:
            return False
        return True
