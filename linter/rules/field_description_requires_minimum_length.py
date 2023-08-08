from linter.rule import Rule
from typing import Any, Tuple


class FieldDescriptionRequiresMinimumLength(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ("dimension", "measure")

    def run(self, field: Any) -> bool:
        length = self.params["min_length"]
        if field.get("hidden") != "yes" and "description" in field:
            if len(field["description"]) < length:
                return False
        return True
