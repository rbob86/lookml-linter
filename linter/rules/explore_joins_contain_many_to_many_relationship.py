from linter.rule import Rule


class ExploreJoinsContainManyToManyRelationship(Rule):
    def applies_to():
        return ('explore',)

    def run(self, explore):
        joins = explore.get('joins', [])
        for join in joins:
            if 'relationship' in join:
                if join['relationship'] == "many_to_many":
                    return False
        return True
