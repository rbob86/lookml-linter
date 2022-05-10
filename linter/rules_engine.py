from typing import Dict
from linter.rule_factory import RuleFactory
from linter.rule_names import RuleNames


class RulesEngine:
    def __init__(self, config: Dict) -> None:
        rules_by_object_type = {}
        rule_factory = RuleFactory()
        config_by_rule_name = {c['rule']: c for c in config}
        for rule_name in RuleNames.get():
            # Apply config overrides
            if rule_name in config_by_rule_name:
                severity = config_by_rule_name[rule_name]['severity']
            # Instantiate rule
            rule = rule_factory.build(rule_name, severity)
            # Add rule to dict once per each object type it applies to
            for object_type in rule.__class__.applies_to():
                rules_by_object_type.setdefault(object_type, []).append(rule)
        self.rules = rules_by_object_type
