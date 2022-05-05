from linter.rules.rule import Rule
from linter.rules.view_should_have_z import ViewShouldHaveZ
from linter.rules.field_should_have_description import FieldShouldHaveDescription


class RuleFactory:
    def __init__(self):
        pass

    def build(self, rule_name: str) -> Rule:
        classname = self.__rule_name_to_classname(rule_name)
        return globals()[classname]()

    def __rule_name_to_classname(self, rule_name: str) -> str:
        return rule_name.replace('_', ' ').title().replace(' ', '')
