import sys
import os
import argparse
from linter.config_validator import ConfigValidator
from linter.lookml_linter import LookMlLinter
from linter.rules_engine import RulesEngine
from linter.lookml_project_parser import LookMlProjectParser


def main():
    config_file = os.environ['INPUT_CONFIGFILE']
    path = os.environ['INPUT_LOOKMLPROJECT']
    

    validator = ConfigValidator(config_file)
    validator.validate()
    config = validator.config
    rules = RulesEngine(config).rules
    LookMlProjectParser.root_file_path = path
    data = LookMlProjectParser().get_parsed_lookml_files()
    linter = LookMlLinter(data, rules)
    linter.run()
    linter.print_errors()


main()
