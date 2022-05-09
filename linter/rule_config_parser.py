import os
import yaml
from pathlib import Path
from typing import List

from jsonschema import validate as validate_json_schema

from linter.rule_factory import RuleFactory
from linter.severity import Severity


class RuleConfigParser:
    rules_dir = os.path.dirname(__file__) + '/rules'

    def __init__(self, config_file):
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            raise Exception(f'Config file at {config_file} not found')

        self.rule_names = self.__get_rule_names()
        override_schema = {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'rule': {
                        'type': 'string',
                        'enum': [name for name in self.rule_names]
                    },
                    'severity': {
                        'type': 'string',
                        'enum': [severity.value for severity in Severity]
                    },
                },
                'required': ['rule', 'severity']
            }
        }
        validate_json_schema(self.config, override_schema)

    def parse(self) -> None:
        rules_by_object_type = {}
        rule_factory = RuleFactory()
        config_by_rule_name = {c['rule']: c for c in self.config}
        for rule_name in self.rule_names:
            severity = None
            if rule_name in config_by_rule_name:
                severity = config_by_rule_name[rule_name]['severity']
            rule = rule_factory.build(rule_name, severity)
            for object_type in rule.__class__.applies_to():
                rules_by_object_type.setdefault(object_type, []).append(rule)
        return rules_by_object_type

    def __get_rule_names(self) -> List[str]:
        dir = RuleConfigParser.rules_dir
        rule_names = [Path(f).stem for f in os.listdir(
            dir) if os.path.isfile(os.path.join(dir, f)) and f != '__init__.py']
        return rule_names
