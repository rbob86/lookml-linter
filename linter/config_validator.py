import os
import yaml
from jsonschema import validate as validate_json_schema
from linter.rules_engine import RulesEngine
from linter.rule import ParamSet, Severity


class ConfigValidator:
    def __init__(self, config_file: str) -> None:
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                self.config = yaml.safe_load(f)
        else:
            raise Exception(f'Config file at {config_file} not found')

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

                        # TODO: Runs extremely slowly, figure out solution
                        # 'items': {
                        #     'type': 'object',
                        #     'properties': {
                        #         'user_attribuste': {'type': 'number'},
                        #         # 'search_terms': {
                        #         #     'type': 'array',
                        #         #     'items': {
                        #         #         'type': 'string'
                        #         #     }
                        #         # },
                        #     }
                        # }
                    }
                },
                'required': ['rule', 'severity']
            }
        }

    def validate(self) -> None:
        validate_json_schema(self.config, self.override_schema)
