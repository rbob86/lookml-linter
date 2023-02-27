import os
from linter.config_validator import ConfigValidator
from linter.lookml_linter import LookMlLinter
from linter.lookml_project_parser import LookMlProjectParser
from linter.rules_engine import RulesEngine


def main():
    # Read in input variables
    config_file = os.environ['INPUT_CONFIGFILE']
    filepaths = os.environ['INPUT_FILEPATHS']

    # Validate config.yaml file
    validator = ConfigValidator(config_file)
    validator.validate()

    # Retrieve rules from config and data from LookML files
    rules = RulesEngine(validator.config).rules
    data = LookMlProjectParser(filepaths).get_parsed_lookml_files()

    if data:
        # Run linter and save/print output
        linter = LookMlLinter(data, rules)
        linter.run()
        error_log = linter.get_errors()
        print(error_log)
        linter.save_errors(error_log, '_lookml-linter-output.txt')

        # Fail GitHub Action only if linter has errors (warnings do not count)
        assert linter.has_errors == False, 'LookML Linter detected an error warning, please resolve any error warning to complete Pull Request'
    elif filepaths:
        print('No .lkml files changed.')
    else:
        print('No .lkml files found in project.')

main()
