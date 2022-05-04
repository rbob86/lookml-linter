
from ruleset import Ruleset
from rule_factory import RuleFactory
from typing import Dict, List


class LookMlLinter:
    def __init__(self, data: Dict, config: List):
        Ruleset.apply_severity_overrides(config)
        self.__init_rules(Ruleset.rules_to_apply())
        self.data = data

    def run(self) -> None:
        views = self.data['views']

        for v in views:
            self.__lint_object(v, 'view')

            for e in v['explores']:
                self.__lint_object(e, 'explore')
            for d in v['dimensions']:
                self.__lint_object(d, 'dimension')
            for g in v['dimension_groups']:
                self.__lint_object(g, 'dimension_group')
            for m in v['measures']:
                self.__lint_object(m, 'measure')

    def __init_rules(self, rules: List) -> None:
        self.rules = {}
        factory = RuleFactory()
        for rule in rules:
            instance_of_rule = factory.build(rule['name'])
            object_types = rule['object_type'] if type(
                rule['object_type']) is tuple else (rule['object_type'],)
            for object_type in object_types:
                self.rules.setdefault(object_type, []).append(instance_of_rule)

    def __lint_object(self, object: Dict, object_type: str) -> None:
        for rule in self.rules[object_type]:
            rule.run(object)
