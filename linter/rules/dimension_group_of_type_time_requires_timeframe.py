from linter.rule import Rule


class DimensionGroupOfTypeTimeRequiresTimeframe(Rule):
    def applies_to():
        return ("dimension_group",)

    def run(self, dimension_group):
        type = dimension_group.get("type")
        if type == "time" and (
            not "timeframe" in dimension_group and not "timeframes" in dimension_group
        ):
            return False
        return True
