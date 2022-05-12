import functools
from os import path, listdir
from pathlib import Path
from typing import Dict, List
from linter.rule_factory import RuleFactory


class RulesEngine:
    rules_dir = path.dirname(__file__) + '/rules'

    def __init__(self, config: Dict) -> None:
        rules_by_object_type = {}
        rule_factory = RuleFactory()
        config_by_rule_name = {c['rule']: c for c in config}
        for rule_name in RulesEngine.rule_names()():
            # Apply config overrides
            if rule_name in config_by_rule_name:
                severity = config_by_rule_name[rule_name]['severity']
            # Instantiate rule
            rule = rule_factory.build(rule_name, severity)
            # Add rule to dict once per each object type it applies to
            for object_type in rule.__class__.applies_to():
                rules_by_object_type.setdefault(object_type, []).append(rule)
        self.rules = rules_by_object_type

    @staticmethod
    @functools.lru_cache
    def rule_names() -> List[str]:
        dir = RulesEngine.rules_dir
        return [Path(f).stem for f in listdir(
                dir) if path.isfile(path.join(dir, f)) and f != '__init__.py']
