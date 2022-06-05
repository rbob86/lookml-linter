import os
import yaml
from jsonschema import validate as validate_json_schema
from linter.rule import Severity
from linter.rules_engine import RulesEngine


class ConfigValidator:
    def __init__(self, config_file: str) -> None:
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            raise FileNotFoundError(f'Config file at {config_file} not found')

        self.override_schema = {
            'type': 'array',
            'items': {
                'type': 'object',
                'properties': {
                    'rule': {
                        'type': 'string',
                        'enum': [name for name in RulesEngine.rule_names()]
                    },
                    'severity': {
                        'type': 'string',
                        'enum': [severity.value for severity in Severity]
                    },
                    'param_sets': {
                        'type': 'array',
                        'items': {
                            'type': 'object'
                        }
                    }
                },
                'required': ['rule', 'severity']
            }
        }

    def validate(self) -> None:
        validate_json_schema(self.config, self.override_schema)
