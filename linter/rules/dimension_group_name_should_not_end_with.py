from linter.rule import Rule
from typing import Any, Tuple


class DimensionGroupNameShouldNotEndWith(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('dimension_group',)

    def run(self, dimension_group: Any) -> bool:
        search_terms = self.params['search_terms']
        search_terms_match_dimension_group_name = any([
            dimension_group.get('name').endswith(term) for term in search_terms])
        return not search_terms_match_dimension_group_name
