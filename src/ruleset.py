from jsonschema import validate as validate_json_schema
from enum import Enum


class Severity(Enum):
    ERROR = 'error'
    WARNING = 'warning'
    IGNORE = 'ignore'


class Ruleset:
    # Prevent direct instantiation
    def __new__(cls, *args, **kwargs):
        if cls is Ruleset:
            raise TypeError(f"Ruleset may not be instantiated")

    rules = (
        {
            "name": "field_should_have_description",
            "object_type": ("dimension", "measure"),
            "severity": Severity.ERROR
        },
        {
            "name": "dimension_should_have_x",
            "object_type": "dimension",
            "severity": Severity.ERROR
        },
        {
            "name": "measure_should_have_y",
            "object_type": "measure",
            "severity": Severity.ERROR
        },
        {
            "name": "view_should_have_z",
            "object_type": "view",
            "severity": Severity.ERROR
        },
        {
            "name": "view_requires_abc",
            "object_type": "view",
            "severity": Severity.WARNING
        },
        {
            "name": "view_requires_xyz",
            "object_type": "view",
            "severity": Severity.ERROR
        },
    )

    override_schema = {
        'type': 'array',
        'items': {
            'type': 'object',
            'properties': {
                'rule': {'type': 'string'},
                'severity': {'type': 'string'},
            },
            'required': ['rule', 'severity']
        }
    }

    @staticmethod
    def rules_to_apply():
        return [rule for rule in Ruleset.rules if rule['severity'] != Severity.IGNORE.value]

    @staticmethod
    def apply_severity_overrides(overrides):
        Ruleset.__validate_severity_overrides(overrides)
        overrides_by_rule_name = {o['rule']: o for o in overrides}
        for rule in Ruleset.rules:
            rule_name = rule['name']
            if rule_name in overrides_by_rule_name:
                rule['severity'] = overrides_by_rule_name[rule_name]['severity']

    @staticmethod
    def __validate_severity_overrides(overrides):
        validate_json_schema(overrides, Ruleset.override_schema)
        Ruleset.__validate_override_rule_names(overrides)
        Ruleset.__validate_override_severities(overrides)

    @staticmethod
    def __validate_override_rule_names(overrides):
        rule_names = [r['name'] for r in Ruleset.rules]
        override_rule_names = [o['rule'] for o in overrides]
        if not all(rule_name in rule_names for rule_name in override_rule_names):
            raise Exception(
                '\n\nRule overrides invalid.  Rule names must be a subset of the following list:\n\t' +
                '\n\t'.join(rule_names) + '\n')

    @staticmethod
    def __validate_override_severities(overrides):
        severities = [s.value for s in Severity]
        override_severities = [o['severity'] for o in overrides]
        if not all(severity in [s.value for s in Severity] for severity in override_severities):
            raise Exception('\n\nOverride severities can only be one of the following:\n\t' +
                            '\n\t'.join(severities) + '\n')
