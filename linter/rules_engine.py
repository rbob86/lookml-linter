import functools
from os import path, listdir
from pathlib import Path
from typing import Dict, List
from linter.rule_factory import RuleFactory


class RulesEngine:
    rules_dir = path.dirname(__file__) + '/rules'

    def __init__(self, config: Dict) -> None:
        rule_factory = RuleFactory()
        config_by_rule_name = {c['rule']: c for c in config}
        self.rules = {}
        for rule_name in RulesEngine.rule_names():
            config_for_rule = config_by_rule_name[rule_name]
            severity = config_for_rule['severity']
            param_sets = config_for_rule['param_sets'] if 'param_sets' in config_for_rule else None
            # Instantiate rule with config attributes applied
            if param_sets:
                for params in param_sets:
                    rule = rule_factory.build(rule_name, severity, params)
                    self.__add(rule, rule_name)
            else:
                rule = rule_factory.build(rule_name, severity)
                self.__add(rule, rule_name)

    @staticmethod
    @functools.lru_cache
    def rule_names() -> List[str]:
        dir = RulesEngine.rules_dir
        return [Path(f).stem for f in listdir(
                dir) if path.isfile(path.join(dir, f)) and Path(f).stem != '__init__']

    def __add(self, rule, rule_name: str) -> None:
        for object_type in rule.__class__.applies_to():
            self.rules.setdefault(object_type, []).append({
                'name': rule_name,
                'instance': rule
            })
