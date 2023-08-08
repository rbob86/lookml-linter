from linter.rule import Rule
from typing import Any, Tuple


class ExploreDescriptionRequiresMinimumLength(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ("explore",)

    def run(self, explore: Any) -> bool:
        length = self.params["min_length"]
        if not "description" in explore:
            return True
        if len(explore["description"]) < length:
            return False
        return True
