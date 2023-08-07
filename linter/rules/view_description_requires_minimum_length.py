from linter.rule import Rule
from typing import Any, Tuple


class ViewDescriptionRequiresMinimumLength(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ("view",)

    def run(self, view: Any) -> bool:
        length = self.params["min_length"]
        if not "description" in view:
            return True
        if len(view["description"]) < length:
            return False
        return True
