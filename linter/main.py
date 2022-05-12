import sys
from linter.config_validator import ConfigValidator
from linter.lookml_linter import LookMlLinter
from linter.rules_engine import RulesEngine
from linter.lookml_project_parser import LookMlProjectParser


def main():
    args = sys.argv[1:]

    config_file = None
    if len(args) > 0:
        config_file = args[0]

    validator = ConfigValidator(config_file)
    validator.validate()
    config = validator.config
    rules = RulesEngine(config).rules
    data = LookMlProjectParser().get_parsed_lookml_files()
    LookMlLinter(data, rules).run()


main()
