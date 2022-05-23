from linter.rule import Rule


class ExploreJoinsRequireRelationship(Rule):
    def applies_to():
        return ('explore',)

    def run(self, explore):
        joins = explore.get('joins', [])
        for join in joins:
            if not 'relationship' in join:
                return False
        return True
