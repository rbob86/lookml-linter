from linter.rule import Rule


class ViewWithDimensionsAndMeasuresHasOnePrimaryKey(Rule):
    def applies_to():
        return ('view',)

    def run(self, view):
        dimensions, measures = [
            view.get(key, []) for key in ['dimensions', 'measures']]
        if len(measures) > 0 and len(dimensions) > 0:
            primary_key_count = 0
            for dimension in dimensions:
                if 'primary_key' in dimension:
                    primary_key_count += 1
            if primary_key_count != 1:
                return False
        return True
